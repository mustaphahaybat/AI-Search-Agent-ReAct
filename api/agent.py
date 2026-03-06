import os
import json
import re
import operator
from typing import Annotated, TypedDict, List
from groq import Groq
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv

load_dotenv()

# Groq Kurulumu
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL_ID = "llama-3.3-70b-versatile"

class AgentState(TypedDict):
    input_text: str
    messages: Annotated[List[dict], operator.add]
    draft: str
    feedback: str
    is_approved: bool

def generator_node(state: AgentState):
    print("--- [GENERATOR] GROQ (LLAMA 3.3) ÇALIŞIYOR ---")
    prompt = f"Sen profesyonel bir tıbbi asistansın. Teşhis koymadan şu belirtileri özetle: {state['input_text']}"
    if state.get("feedback"):
        prompt += f"\n\nEleştiriye göre düzelt: {state['feedback']}"
    
    completion = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}]
    )
    new_draft = completion.choices[0].message.content
    return {
        "draft": new_draft,
        "messages": [{"role": "assistant", "content": f"[Generator]: {new_draft}"}]
    }

def critic_node(state: AgentState):
    print("--- [CRITIC] GROQ (LLAMA 3.3) ÇALIŞIYOR ---")
    prompt = f"""
    Şu tıbbi özeti denetle: {state['draft']}
    JSON formatında cevap ver: {{"is_approved": true, "feedback": ""}}
    """
    completion = client.chat.completions.create(
        model=MODEL_ID,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    result = json.loads(completion.choices[0].message.content)
    return {
        "is_approved": result.get("is_approved", False),
        "feedback": result.get("feedback", ""),
        "messages": [{"role": "assistant", "content": f"[Critic]: {result}"}]
    }

def should_continue(state: AgentState):
    if state["is_approved"]: return END
    return "generator"

workflow = StateGraph(AgentState)
workflow.add_node("generator", generator_node)
workflow.add_node("critic", critic_node)
workflow.set_entry_point("generator")
workflow.add_edge("generator", "critic")
workflow.add_conditional_edges("critic", should_continue)
app = workflow.compile()
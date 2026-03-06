from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import app  # Değişen satır burası (Changed line)
import uuid

main_app = FastAPI(title="Medical Agent API")

class AnalyzeRequest(BaseModel):
    text: str

@main_app.get("/health")
def health_check():
    return {"status": "ok"}

@main_app.post("/analyze")
async def analyze_symptoms(request: AnalyzeRequest):
    try:
        initial_state = {
            "input_text": request.text,
            "messages": [],
            "is_approved": False
        }
        result = app.invoke(initial_state, config={"recursion_limit": 10})
        return {
            "final_summary": result.get("draft", ""),
            "history": [msg["content"] for msg in result.get("messages", [])]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
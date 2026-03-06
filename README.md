# 🤖 AI-Search-Agent-ReAct: Autonomous Clinical & General Search Agent

An advanced AI agent architecture that leverages the **ReAct (Reasoning + Acting)** pattern to perform real-time web searches and provide grounded, up-to-date answers. Built with **LangChain**, **Groq (LPU)**, and **FastAPI**.



## 🌟 Key Features
- **ReAct Framework:** Uses a "Thought-Action-Observation" loop to decide when to search the web.
- **Lightning Fast Inference:** Powered by **Groq LPU** and **Llama-3.1-70B** for near-instant responses.
- **Specialized Search:** Integrated with **Tavily Search API** for noise-free, AI-optimized results.
- **Production Ready:** Fully containerized using **Docker** and **Docker Compose**.
- **Modern UI:** Clean and responsive chat interface built with **Streamlit**.

## 🏗️ Architecture
The project follows a microservices pattern:
- **Backend (FastAPI):** Orchestrates the LangGraph/LangChain logic and tool invocations.
- **Frontend (Streamlit):** Handles user interactions and displays real-time agent "thoughts".



## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose installed.
- Groq API Key & Tavily API Key.

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/AI-Search-Agent-ReAct.git](https://github.com/YOUR_USERNAME/AI-Search-Agent-ReAct.git)
   cd AI-Search-Agent-ReAct

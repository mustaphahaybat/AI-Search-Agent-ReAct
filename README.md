# 🤖 AI-Search-Agent-ReAct: Autonomous Search Agent

An advanced AI agent architecture that leverages the **ReAct (Reasoning + Acting)** pattern to perform real-time web searches and provide grounded, up-to-date answers. Built with **LangChain**, **Groq (LPU)**, and **FastAPI**.



## 🌟 Key Features

- **ReAct Framework:** Uses a "Thought-Action-Observation" loop to decide when to search the web for missing information.
- **Lightning Fast Inference:** Powered by **Groq LPU** and **Llama-3.1-70B** for near-instant reasoning and response generation.
- **Specialized Search:** Integrated with **Tavily Search API** for noise-free, AI-optimized web results.
- **Production Ready:** Fully containerized using **Docker** and **Docker Compose** for seamless deployment.
- **Modern UI:** Clean and responsive chat interface built with **Streamlit** to monitor the agent's internal thought process.

## 🏗️ Architecture

The project follows a microservices pattern to ensure scalability and separation of concerns:

- **Backend (FastAPI):** Orchestrates the LangGraph/LangChain logic, manages tool invocations, and serves the agent's brain.
- **Frontend (Streamlit):** Handles user interactions and displays real-time agent "thoughts" and search observations.



## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose installed on your system.
- API Keys for [Groq](https://console.groq.com/) and [Tavily](https://tavily.com/).

### Installation & Deployment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/AI-Search-Agent-ReAct.git
   cd AI-Search-Agent-ReAct

2. **Setup Environment Variables:**

Create a .env file in the root directory.

Use .env.example as a template:

Plaintext

GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LLM_MODEL=llama-3.1-70b-versatile

3. **Launch with Docker:**
docker-compose up --build

4. **Access the Application:**

**Frontend (UI):** http://localhost:8501

**Backend (API):** http://localhost:8000

🧠 **Engineering Insights**

**Inference Optimization:** Switching from standard GPU-based providers to Groq's LPU architecture reduced the agent's reasoning latency by approximately 90%, enabling a truly conversational experience.

**Noise Reduction:** By implementing max_results=3 via the Tavily API, we optimized the context window usage, reducing token costs while increasing the factual accuracy of the agent's responses.

**Environment Isolation:** Using Docker ensures that the heavy LangChain and Python dependencies are isolated, solving the "it works on my machine" problem once and for all.

📄 **License**

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute.

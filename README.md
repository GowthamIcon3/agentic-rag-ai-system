# agentic-rag-ai-system
## Multi-Agent RAG AI System using CrewAI, Gemini, and Tavily

This project demonstrates a **production-style multi-agent AI system** built using modern generative AI technologies such as **CrewAI, Google Gemini, Tavily Search API, and Retrieval-Augmented Generation (RAG)** with a **Chroma vector database**.

The system is designed to simulate how real-world AI applications orchestrate multiple specialized agents to solve complex tasks. Instead of relying on a single large language model prompt, the workflow is divided among **collaborating AI agents**, each responsible for a specific role such as planning, research, knowledge retrieval, and content generation.

The architecture combines **tool-augmented reasoning and retrieval-based grounding**, enabling the system to access both **real-time web information and internal knowledge sources** before generating responses. This approach significantly improves factual accuracy, reduces hallucinations, and enables domain-specific responses.

The application integrates:

* **CrewAI** for multi-agent orchestration
* **Google Gemini (gemini-1.5-flash)** as the core reasoning LLM
* **Tavily Search API** for real-time web research
* **Chroma Vector Database** for semantic retrieval
* **Sentence Transformer Embeddings** for vector similarity search
* **Streamlit** for an interactive AI web application interface

### Workflow Overview

User Input → Planner Agent → Research Agent (Tavily Search) → RAG Retrieval (Chroma Vector Database) → Writer Agent → Final AI Response

### Key Objectives of the Project

* Demonstrate **agent-based AI system design**
* Implement **retrieval-augmented generation (RAG)** to reduce hallucinations
* Integrate **external tools for real-time data retrieval**
* Build a **modular, production-ready AI application architecture**
* Showcase practical skills in **LLM orchestration and AI workflow automation**

This project reflects the architecture commonly used in **modern enterprise AI applications**, including AI research assistants, enterprise knowledge bots, and intelligent automation systems.


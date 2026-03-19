<div align="center">

<img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
<img src="https://img.shields.io/badge/FAISS-Vector_Search-0057B7?style=for-the-badge" />
<img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=google&logoColor=white" />

<br/>
<br/>

# 🧠 LLM-Based Resume Analyzer + Chatbot

**Upload your resume. Paste a job description. Get AI-powered analysis, match scoring, and a chatbot that knows your resume inside-out.**

[![Live App](https://img.shields.io/badge/🌐_Live_App-Click_to_Open-FF4B4B?style=for-the-badge)](https://llm-resume-analyzer.streamlit.app/)

[Overview](#-overview) · [Features](#-features) · [Architecture](#-architecture) · [How It Works](#-how-it-works) · [Installation](#-run-locally) · [Structure](#-project-structure)

</div>

---

## 📌 Overview

The **LLM-Based Resume Analyzer** is a Generative AI application that helps job seekers optimize their resumes for specific roles. Upload a PDF resume, paste a job description, and the system uses **RAG (Retrieval-Augmented Generation)** with **FAISS vector search** and **Google Gemini** to deliver deep analysis — plus a conversational chatbot to answer questions about your resume.

> 💡 *Built for job seekers who want more than keyword matching — this system understands context, identifies gaps, and suggests real improvements.*

---

## ✨ Features

- 📄 **PDF Resume Parsing** — Extracts and processes content from uploaded resumes
- 🎯 **JD Match Scoring** — Semantic similarity between your resume and the job description
- 🔍 **Skills Gap Detection** — Identifies missing skills and qualifications
- 💡 **Improvement Suggestions** — Actionable, role-specific recommendations
- 🤖 **Resume Chatbot** — Ask anything about your resume in natural language
- 🧩 **RAG Architecture** — Retrieval-Augmented Generation for grounded, accurate responses
- 🗂️ **FAISS Vector Store** — Fast semantic search over resume content

---

## 🏗 Architecture

```
PDF Resume
    │
    ▼
Text Extraction → Chunking → Embeddings (Gemini)
                                    │
                                    ▼
                            FAISS Vector Store ◄──── vectorstore.py
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
               query.py                        chatbot.py
          (Analysis Engine)              (Conversational RAG)
                    │                               │
                    └───────────────┬───────────────┘
                                    │
                                 app.py
                            (Streamlit UI)
```

### Component Breakdown

| File | Role |
|---|---|
| `app.py` | Main Streamlit UI — handles upload, inputs, and displays results |
| `vectorstore.py` | Builds and persists the FAISS vector store from resume chunks |
| `query.py` | Runs semantic analysis — match score, gap detection, suggestions |
| `chatbot.py` | Conversational RAG chain for the interactive resume chatbot |

---

## 🧠 How It Works

1. **Upload** your resume (PDF) and paste the target job description
2. **Chunking & Embedding** — Resume is split into semantic chunks and embedded via Gemini
3. **Vector Store** — Chunks are indexed in FAISS for fast retrieval
4. **Analysis** — `query.py` retrieves relevant chunks and prompts Gemini to generate:
   - JD match score
   - Missing skills and experience gaps
   - Specific improvement suggestions
5. **Chatbot** — `chatbot.py` powers a RAG-based Q&A loop so you can ask follow-up questions grounded in your actual resume content

---

## 🛠 Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.9+ |
| LLM & Embeddings | Google Gemini API |
| Orchestration | LangChain |
| Vector Search | FAISS (Facebook AI Similarity Search) |
| PDF Parsing | PyPDF2 / LangChain Document Loaders |
| Frontend | Streamlit |
| Config | python-dotenv |

---

## 📁 Project Structure

```
llm-resume-analyzer/
│
├── app.py                  # Streamlit UI & main entry point
├── chatbot.py              # RAG-based conversational chatbot
├── query.py                # Resume analysis & JD matching logic
├── vectorstore.py          # FAISS vector store creation & loading
│
├── .env                    # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

### Prerequisites
- Python 3.9+
- Google Gemini API key ([get one here](https://aistudio.google.com/app/apikey))

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/Ayush-jais05/llm-resume-analyzer.git
cd llm-resume-analyzer

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API key
echo "GOOGLE_API_KEY=your_gemini_api_key_here" > .env

# 5. Run the app
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 💬 Usage

1. Open the app (live or local)
2. **Upload** your resume as a PDF
3. **Paste** the job description you're targeting
4. Click **Analyze** to get:
   - Match score
   - Skill gaps
   - Actionable suggestions
5. Switch to the **Chatbot** tab to ask follow-up questions about your resume

---

## 🔮 Roadmap

- [ ] Support DOCX resume format
- [ ] ATS (Applicant Tracking System) keyword optimization
- [ ] Multi-resume comparison mode
- [ ] Export analysis report as PDF
- [ ] Resume rewriting suggestions with inline diffs
- [ ] Support for multiple LLM providers (OpenAI, Claude)

---

## 👨‍💻 Author

**Ayush Raj**  
Built to demonstrate applied RAG architecture — combining vector search, LLM orchestration with LangChain, and conversational AI in a practical, real-world use case.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

Found this useful? Give it a ⭐ on GitHub — it means a lot!

</div>
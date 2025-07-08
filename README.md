# StudyPilot – AI-Powered Academic Assistant

A free, open-source tool for students to upload their notes/PDFs and ask questions. Built with FastAPI, sentence-transformers, FAISS, and optionally connected to free LLM APIs like OpenRouter.

---

## ✨ Features

- 📄 Upload academic PDFs
- 📚 Extract & embed content using sentence-transformers
- 🔍 Search notes using semantic similarity
- 🤖 Ask questions and get context-aware answers using free LLMs

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

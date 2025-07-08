from fastapi import FastAPI, UploadFile, File
from app.pdf_parser import extract_text_from_pdf
from app.embedder import embed_text
from app.vector_store import save_embeddings
from app.ask_question import handle_question

app = FastAPI()

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text_chunks = extract_text_from_pdf(content)
    embeddings = embed_text(text_chunks)
    save_embeddings(embeddings, text_chunks)
    return {"message": f"{len(text_chunks)} chunks embedded and stored."}

@app.post("/ask/")
def ask_question(q: str):
    answer = handle_question(q)
    return {"answer": answer}

# Optional block to allow running with: python app/main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

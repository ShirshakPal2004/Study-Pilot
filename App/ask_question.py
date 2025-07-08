from app.embedder import embed_question
from app.vector_store import search_similar_chunks
from app.llm import generate_answer

def handle_question(question: str):
    question_vector = embed_question(question)
    top_chunks = search_similar_chunks(question_vector)
    return generate_answer(question, top_chunks)

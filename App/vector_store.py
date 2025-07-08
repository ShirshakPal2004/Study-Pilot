import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)

# Store original text chunks so we can retrieve them
stored_chunks = []

def save_embeddings(embeddings: np.ndarray, texts: list):
    global stored_chunks
    index.add(embeddings)
    stored_chunks.extend(texts)

def search_similar_chunks(query_vector: np.ndarray, k: int = 3):
    D, I = index.search(query_vector, k)
    return [stored_chunks[i] for i in I[0] if i < len(stored_chunks)]

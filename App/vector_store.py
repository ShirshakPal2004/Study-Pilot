import faiss
import numpy as np

# Simple FAISS index stored in memory
dimension = 384  # MiniLM's output dim
index = faiss.IndexFlatL2(dimension)

def save_embeddings(embeddings: np.ndarray, texts: list):
    index.add(embeddings)
    # Optional: save texts separately or map index IDs
    print(f"Stored {len(texts)} vectors.")

def search_similar_chunks(query_vector: np.ndarray, k: int = 3):
    D, I = index.search(query_vector, k)
    # In real app you'd map index IDs to text chunks. For now just return placeholders.
    return [f"Relevant chunk {i}" for i in I[0]]

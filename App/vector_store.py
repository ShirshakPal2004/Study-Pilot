import faiss
import numpy as np

# Simple FAISS index stored in memory
dimension = 384  # MiniLM's output dim
index = faiss.IndexFlatL2(dimension)

def save_embeddings(embeddings: np.ndarray, texts: list):
    index.add(embeddings)
    # Optional: save texts separately or map index IDs
    print(f"Stored {len(texts)} vectors.")

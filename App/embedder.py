from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(chunks: List[str]) -> np.ndarray:
    return model.encode(chunks)

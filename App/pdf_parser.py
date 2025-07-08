import fitz  # PyMuPDF
from typing import List
import io

def extract_text_from_pdf(file_bytes: bytes) -> List[str]:
    doc = fitz.open(stream=io.BytesIO(file_bytes), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return [text[i:i+500] for i in range(0, len(text), 500)]

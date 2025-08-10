"""Parses uploaded files and chunks text."""
import uuid
import io
from app.utils.chunking import chunk_text
from app.config.settings import settings

try:
    import pdfplumber
except Exception:
    pdfplumber = None

try:
    import docx
except Exception:
    docx = None

try:
    from email import policy
    from email.parser import BytesParser
except Exception:
    BytesParser = None

def _extract_text_from_bytes(content: bytes, filename: str) -> str:
    lower = filename.lower()
    if lower.endswith('.pdf') and pdfplumber:
        try:
            with pdfplumber.open(io.BytesIO(content)) as pdf:
                pages = [p.extract_text() or '' for p in pdf.pages]
                return '\n'.join(pages)
        except Exception:
            pass

    if lower.endswith('.docx') and docx:
        try:
            from docx import Document
            f = io.BytesIO(content)
            doc = Document(f)
            text = '\n'.join(p.text for p in doc.paragraphs)
            return text
        except Exception:
            pass

    if lower.endswith('.eml') and BytesParser:
        try:
            msg = BytesParser(policy=policy.default).parsebytes(content)
            if msg.is_multipart():
                parts = [
                    p.get_payload(decode=True).decode('utf-8', errors='ignore')
                    for p in msg.walk() if p.get_content_type() == 'text/plain'
                ]
                return '\n'.join(parts)
            else:
                return msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        except Exception:
            pass

    try:
        return content.decode('utf-8', errors='ignore')
    except Exception:
        return str(content)

def parse_and_chunk(content: bytes, filename: str):
    text = _extract_text_from_bytes(content, filename)
    if not text or not text.strip():
        return []

    chunks = chunk_text(text, max_chars=settings.MAX_CHUNK_CHARS)
    out = []
    for i, c in enumerate(chunks):
        out.append({
            "id": f"{filename}-{i}-{uuid.uuid4().hex[:8]}",
            "text": c,
            "meta": {"source": filename, "chunk_index": i, "text": (c[:200] + '...') if len(c) > 200 else c}
        })
    return out

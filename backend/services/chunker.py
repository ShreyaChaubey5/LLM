from utils.config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_text(text: str) -> list:
    """
    Splits text into chunks of CHUNK_SIZE with CHUNK_OVERLAP characters.
    Returns a list of text chunks.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + CHUNK_SIZE
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks

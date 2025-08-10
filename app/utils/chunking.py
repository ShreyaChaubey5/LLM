"""Simple text chunker. Replace with token-aware chunking for production."""
def chunk_text(text: str, max_chars: int = 2000):
    chunks = []
    start = 0
    length = len(text)
    while start < length:
        end = min(start + max_chars, length)
        chunk = text[start:end]
        if end < length:
            extra_end = end
            tail = text[end:end+200]
            nxt_nl = tail.find('\n')
            nxt_space = tail.find(' ')
            candidates = [p for p in (nxt_nl, nxt_space) if p >= 0]
            if candidates:
                shift = min(candidates)
                extra_end = end + shift + 1
                chunk = text[start:extra_end]
                start = extra_end
            else:
                start = end
        else:
            start = end
        chunks.append(chunk)
    return chunks

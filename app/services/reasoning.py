"""Call Gemini Pro with context + query to produce structured JSON output."""
from app.config.settings import settings
import json, re

try:
    import google.generativeai as genai
    genai.configure(api_key=settings.GOOGLE_API_KEY)
except Exception:
    genai = None

_PROMPT = '''
You are an insurance decision assistant. Use the provided context (clauses/excerpts) to answer the question.

Context:
{context}

Question: {query}

Return a JSON object with keys: decision, justification, referenced_clauses (array of ids).
Make sure the output is valid JSON only. Do not include extra commentary.
'''

def _extract_json_from_text(text: str):
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\{[\s\S]*\}", text)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                return {"raw": text}
        return {"raw": text}

def call_gemini_reasoner(query: str, matches: list):
    context_pieces = []
    for m in matches:
        meta = m.get('meta', {})
        text_snippet = meta.get('text') or meta.get('excerpt') or ''
        context_pieces.append(f"[{m['id']}] {text_snippet}")

    context = "\n---\n".join(context_pieces)
    prompt = _PROMPT.format(context=context, query=query)

    if genai is None:
        return {"decision": "unknown", "justification": "Generative AI client not configured", "referenced_clauses": []}

    resp = genai.chat.create(model=settings.REASONING_MODEL, messages=[{"role": "user", "content": prompt}], max_output_tokens=512)

    # extract textual content robustly
    text = ""
    if isinstance(resp, dict):
        if 'candidates' in resp and len(resp['candidates']) > 0:
            text = resp['candidates'][0].get('content', '')
        elif 'output' in resp:
            if isinstance(resp['output'], list) and len(resp['output']) > 0 and 'content' in resp['output'][0]:
                text = resp['output'][0]['content']
            else:
                text = str(resp['output'])
        else:
            text = str(resp)
    else:
        text = str(resp)

    parsed = _extract_json_from_text(text)
    if isinstance(parsed, dict) and 'raw' in parsed and len(parsed) == 1:
        return {"decision": "undetermined", "justification": text, "referenced_clauses": []}
    return parsed

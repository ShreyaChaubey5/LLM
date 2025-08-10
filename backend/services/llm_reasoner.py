from openai import OpenAI
from utils.config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_decision(query: str, relevant_chunks: list) -> dict:
    """
    Uses GPT to make a decision based on the query and retrieved clauses.
    Returns a dict with decision, clauses, and justification.
    """
    # Prepare context from retrieved chunks
    context_text = "\n\n".join(relevant_chunks)

    prompt = f"""
You are an insurance policy expert.
You will be given:
1. A user query describing a claim case.
2. Relevant clauses from a policy document.

Your task:
- Decide if the claim should be APPROVED or REJECTED.
- List the relevant clauses.
- Provide a bullet-point justification.

Respond in JSON format with the keys:
decision, clauses (list), justification (list).

User Query:
{query}

Relevant Clauses:
{context_text}
"""

    response = client.chat.completions.create(
        model=genai.GenerativeModel("gemini-pro"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw_text = response.choices[0].message.content.strip()

    try:
        # Try to parse the GPT output as JSON
        import json
        result = json.loads(raw_text)
    except Exception:
        # Fallback if GPT does not output valid JSON
        result = {
            "decision": "Unknown",
            "clauses": relevant_chunks,
            "justification": ["The LLM could not parse a proper decision."]
        }

    return result

from services.vector_store import query_embeddings
from utils.config import GEMINI_MODEL

def retrieve_relevant_chunks(query, top_k=5):
    return query_embeddings(query, top_k)

def generate_answer(query):
    relevant_chunks = retrieve_relevant_chunks(query)
    context_text = "\n".join([c["text"] for c in relevant_chunks])

    prompt = f"""
    You are an AI assistant.
    Based on the following context, answer the question.
    Context:
    {context_text}

    Question:
    {query}
    """

    response = GEMINI_MODEL.generate_content(prompt)
    return {
        "answer": response.text,
        "sources": [c["metadata"] for c in relevant_chunks]
    }

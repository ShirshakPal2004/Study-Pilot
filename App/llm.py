import requests

# Replace with your real key if you use OpenRouter
API_KEY = "your-openrouter-api-key"

def generate_answer(question, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"Use the following notes to answer the question:\n\n{context}\n\nQ: {question}\nA:"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful academic assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return "LLM request failed. Try setting a valid API key or check your internet."

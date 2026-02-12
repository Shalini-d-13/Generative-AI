from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

user_input = input("ask a question:")

messages = [{
    "role": "system",
    "content": "you are an IT engineers assistant. Answer only IT and Computer related questions. If the question is not related to IT or Computer, answer with 'I am sorry, I can only answer IT and Computer related questions.'"
}, {
    "role": "user",
    "content": user_input
}]

response = client.chat.completions.create(
    model="openai/gpt-4",
    messages=messages,
    max_tokens=150
)

print(response.choices[0].message.content)

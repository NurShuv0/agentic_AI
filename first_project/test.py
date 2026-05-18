from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="anything"
)

response = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Explain AI simply"}
    ]
)

print(response.choices[0].message.content)
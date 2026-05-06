import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

diff = open("diff.txt").read()

prompt = f"Review this code diff and suggest improvements:\n{diff}"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)

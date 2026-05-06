
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

diff = open("diff.txt").read()

prompt = f"Review this code diff and suggest improvements:\n{diff}"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

print(response["choices"][0]["message"]["content"])

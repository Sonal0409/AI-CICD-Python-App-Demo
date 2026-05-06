
import openai
import os
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

log_data = sys.argv[1]

prompt = f"Explain this CI/CD failure and suggest fix:\n{log_data}"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

print(response["choices"][0]["message"]["content"])

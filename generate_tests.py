import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

code = open("app.py").read()

prompt = f"Generate pytest test cases for this Flask app:\n{code}"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

tests = response["choices"][0]["message"]["content"]

with open("test_app.py", "w") as f:
    f.write(tests)

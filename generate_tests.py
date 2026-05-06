
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

code = open("app.py").read()

prompt = f"Generate pytest test cases for this Flask app:\n{code}"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

tests = response.choices[0].message.content

with open("test_app.py", "w") as f:
    f.write(tests)

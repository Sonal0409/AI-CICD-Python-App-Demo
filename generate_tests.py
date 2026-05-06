from openai import OpenAI
import os
import ast

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read app code
with open("app.py", "r") as f:
    code = f.read()

# Strong prompt to force valid output
prompt = f"""
Generate ONLY valid pytest test code for this Flask app.

STRICT RULES:
- Output ONLY Python code
- NO explanations
- NO markdown (no ``` blocks)
- Must be directly runnable with pytest
- Use Flask test client
- Include at least one test

Code:
{code}
"""

# Call AI
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

tests = response.choices[0].message.content.strip()

# Cleanup: remove markdown if present
if "```" in tests:
    tests = tests.replace("```python", "").replace("```", "").strip()

# Validate Python syntax
try:
    ast.parse(tests)
    print("AI generated valid Python tests")

except SyntaxError:
    print("Invalid AI output. Using fallback test.")

    tests = """
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
"""

# Save test file
with open("test_app.py", "w") as f:
    f.write(tests)

print("test_app.py created successfully")

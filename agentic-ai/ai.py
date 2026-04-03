# 🤖 Simple Gemini Client (OpenAI-compatible)
import os
from openai import OpenAI

# 🔑 Read API key from environment
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not set")

# 🌐 Create client
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 💬 Message input
messages = [
    {"role": "user", "content": "Hello! Tell me something interesting."}
]

# 🚀 Call model
response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-preview",
    messages=messages
)

# 🖨️ Print response
print(response.choices[0].message.content)

##################################################################
# ✅ Structured evaluation using Pydantic
from pydantic import BaseModel

# 📦 Response schema
class Evaluation(BaseModel):
    is_acceptable: bool
    feedback: str

def evaluate(reply, message, history) -> Evaluation:
    messages = [{"role": "system", "content": evaluator_system_prompt}] + [{"role": "user", "content": evaluator_user_prompt(reply, message, history)}]
    response = gemini.beta.chat.completions.parse(model="gemini-2.5-flash", messages=messages, response_format=Evaluation)
    return response.choices[0].message.parsed

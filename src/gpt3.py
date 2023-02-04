import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("GPTKEY")

prompt = "Write python code to generate random number between 1 to 10"

def code_complete(prompt):
    response = openai.Completion.create(
    model="code-davinci-002",
    prompt=prompt,
    temperature=0,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response

print(code_complete(prompt))
from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "5 best lucrative careers that you can leverage to become entrepreneur later"}
    ]
)

print(completion.choices[0].message)
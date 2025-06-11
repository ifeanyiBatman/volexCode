import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

user_prompt = sys.argv[1]
verbosity = False

#check if second 
if len(sys.argv) > 2:
    if sys.argv[2]  == "--verbose":
        verbosity = True




load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user",parts=[types.Part(text=user_prompt)])
]

#content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
response = client.models.generate_content(
    model='gemini-2.0-flash-001',contents=messages
)

#output to console 
print(response.text)

if verbosity:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

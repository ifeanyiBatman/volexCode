import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from system_prompt import system_prompt
from call_function import call_function , available_functions



user_prompt = sys.argv[1]

verbose = "--verbose" in sys.argv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

def generate_content(client,messages,verbose):

    for i in range(20):
        function_called = False
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions] ,system_instruction=system_prompt),
        )
        
        #print(messages)

        for candidate in response.candidates:
            messages.append(candidate.content)

        function_called = False

        if response.function_calls:
            function_called = True
            parts = []
            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part,verbose=verbose)
                parts.append(function_call_result.parts[0])
            
            # Create tool message for the function responses
            messages.append(
                types.Content(
                    role="tool",
                    parts=parts
                )
            )

            if verbose:
                for part in parts:
                    if part.function_response:
                        print(f"-> Response from {part.function_response.name}:")
                        print(f"{part.function_response.response}")
    
        else:
            if verbose:
                print(f"User prompt: {user_prompt}")


                print(f"-> {response.text}")
                
            else:

                print(response.text)

        if function_called  != True:
            break


    if verbose:
       
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


generate_content(client,messages,verbose)
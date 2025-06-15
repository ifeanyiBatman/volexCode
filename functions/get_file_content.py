import os
from google.genai import types
def get_file_content(working_directory,file_name):
    working_directory = os.path.abspath(working_directory)
    file_name = os.path.abspath(working_directory + '/' + file_name)
    if not file_name.startswith(working_directory):
        return f'Error: Cannot read "{file_name} as it is outside the working directory.'
    if  not os.path.exists(file_name):
        return f"Error: File '{file_name}' does not exist."
    if not os.path.isfile(file_name):
        return f'Error: File not found or is not a regular file: "{file_name}"'
    with open(file_name,'r') as file:
        content =  file.read()
        if len(content) > 10000:
            content = content[:10000] + f'[...File "{file_name}" truncated at 10000 characters]'
        return content
    


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of a given file as a string , with  at most 10,0000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_name": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to read, relative to the working directory.",
            ),
        }
    )
)
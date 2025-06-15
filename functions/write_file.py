import os
import google 
from google.genai import types 

def write_file(working_directory, relative_file_path, content):
    # Ensure working_directory is an absolute path for reliable comparisons
    abs_working_directory = os.path.abspath(working_directory)
    
    # Construct the full, absolute path to the target file.
    # os.path.abspath() also normalizes the path (e.g., resolves '..' components).
    target_abs_path = os.path.abspath(os.path.join(abs_working_directory, relative_file_path))

    # Security check: Ensure the target path is genuinely within the working directory.
    # This prevents writing to files outside the intended scope (e.g., via '..\..\system_file').
    if not target_abs_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{relative_file_path}" as it is outside the permitted working directory "{working_directory}"'

    try:
        # Ensure parent directories for the target file exist.
        # os.makedirs will create intermediate directories if needed; exist_ok=True prevents an error if they already exist.
        os.makedirs(os.path.dirname(target_abs_path), exist_ok=True)
        
        # Open the file in write mode ('w').
        # This will create the file if it doesn't exist, or overwrite/truncate it if it does.
        with open(target_abs_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{relative_file_path}" ({len(content)} characters written)'
    except IOError as e: # Catch file operation errors
        return f'Error writing to file "{relative_file_path}": {e}'
    except Exception as e: # Catch other potential errors (e.g., permissions for makedirs)
        return f'Error: {e} An unexpected error occurred while writing to "{relative_file_path}": {e}'


schema_write_file = types.FunctionDeclaration(
    name = "write_file",
    description="writes to a file , whether it exists or not (creates it) ,  constrained to the working directory",
    parameters=types.Schema(
        type = types.Type.OBJECT,
        properties={
            "relative_file_path": types.Schema(
                type = types.Type.STRING,
                description="The name of the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type = types.Type.STRING,
                description="The content to write to the file.",
            )
        }  
    )
)

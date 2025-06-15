import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    file_name = file_path
    working_directory = os.path.abspath(working_directory)
    file_path = os.path.abspath(working_directory + "/" + file_path)


    if not os.path.exists(file_path):
        return f'Error: File "{file_name}" not found.'

    if not file_path.startswith(working_directory):
        return f'Error: Cannot execute "{file_name}" as it is outside the permitted working directory'

     
    if not os.path.isfile(file_path):
        return f'Error: "{file_path}" is not a file.'
    if not file_path.endswith('.py'):
        return f'Error: File "{file_path}" is not a Python file.'
    
    try:
        process_result = subprocess.run( args=["python",file_path], capture_output=True, text=True, cwd=working_directory, timeout= 30,)

        return f" STDOUT: {process_result.stdout} \n STDERR: {process_result.stderr} \n RETURN CODE: {process_result.returncode}"
    except Exception as e:
        return f"Error: executing file: {e}"
        

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file to run, relative to the working directory.",
            ),
        }
    )
)
    



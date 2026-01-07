import os
import subprocess
from google.genai import types

def run_python_file(working_directory: str, file_path: str, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_file_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_file_path:
            return (
                f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            )

        if not os.path.isfile(target_file):
            return (
                f'Error: "{file_path}" does not exist or is not a regular file'
            )

        if not target_file.endswith(".py"):
            return (
                f'Error: "{file_path}" is not a Python file'
            )

        command = ["python", target_file]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            return f"Error: Process exited with code {result.returncode}"
        elif not result.stdout and not result.stderr:
            return "No output produced"
        else:
            return (f"STDOUT:{result.stdout}\nSTDERR:{result.stderr}")

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a Python file in the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Arguments to pass to the Python file",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
    ),
)

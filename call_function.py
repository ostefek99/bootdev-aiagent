from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.get_files_info import get_files_info
from google.genai import types

def call_function(function_call, verbose=False):
  if verbose:
    print(f"Calling function: {function_call.name}({function_call.args})")
  else:
    print(f" - Calling function: {function_call.name}")

  # define working directory
  working_dir = "calculator"

  function_map = {
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
    "get_files_info": get_files_info,
  }

  function_name = function_call.name or ""

  if function_name in function_map:
    function_result = function_map[function_name](working_dir, **function_call.args)
    return types.Part.from_function_response(
        name=function_name,
        response={"result": function_result},
    )
  else:
    return types.Part.from_function_response(
        name=function_name,
        response={"error": f"Unknown function: {function_name}"},
    )

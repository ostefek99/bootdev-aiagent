import argparse
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
# AI System Prompt definition
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.get_file_content import schema_get_file_content
from call_function import call_function

def generate_content(client, messages, verbose=False):
    """
    Generate content using the Gemini API. Taken from https://googleapis.github.io/python-genai/#generate-content

    Args:
        client: The Gemini client instance
        messages: List of message contents to send to the model

    Returns:
        The generated response from the model
    """
    # Gemini AI model to use
    gemini_ai_model="gemini-2.5-flash"

    # Define available functions
    available_functions = types.Tool(
        function_declarations=[schema_get_files_info, schema_run_python_file, schema_write_file, schema_get_file_content],
    )

    # Configure the model
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )

    response = client.models.generate_content(
        model=gemini_ai_model,
        contents=messages,
        config=config,
    )

    if response is None or response.usage_metadata is None:
        raise RuntimeError("Gemini API response appears to be malformed")

    if response.function_calls:
        for function_call in response.function_calls:
            result = call_function(function_call, verbose)
            print(result)

    if verbose:
        print("User prompt:", messages)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print("Response:")

    print(response.text)


def main() -> None:
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print(
            "Error: GEMINI_API_KEY is not set. Add it to your environment or .env file.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    parser = argparse.ArgumentParser(description="Chatbot")
    # Now we can access `args.user_prompt`
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    try:
        client = genai.Client(api_key=api_key)
        # args.user_prompt is the user's prompt from the command line
        prompt = args.user_prompt

        messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

        # call the generate_content function
        generate_content(client, messages, verbose=args.verbose)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()

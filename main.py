import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from callable_fns import available_functions, call_function

MAX_ITERATIONS = 20


def main():
    args: list[str] = sys.argv[1:]
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt: str = ""
    verbose: bool = False

    if args[-1] == "--verbose":
        user_prompt = " ".join(args[:-1])
        verbose = True
    else:
        user_prompt = " ".join(args)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERATIONS:
            print(f"Maximum iterations ({MAX_ITERATIONS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(
                client, messages, user_prompt, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")


def generate_content(client, messages, user_prompt, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
        )
    )

    if verbose:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose)

        if (not function_call_result.parts or
            not function_call_result.parts[0].function_response or
                not function_call_result.parts[0].function_response.response):
            raise Exception("Invalid function response structure")

        if verbose:
            print(
                f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("No function responses generated, exiting.")

    messages.append(types.Content(role="tool", parts=function_responses))


if __name__ == "__main__":
    main()

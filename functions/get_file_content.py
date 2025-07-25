import os
from google.genai import types

MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(relative_path)

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1)

        if len(file_content_string) > MAX_CHARS:
            # There was more content, so truncate and add message
            file_content_string = file_content_string[:MAX_CHARS] + \
                f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

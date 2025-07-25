import os
from google.genai import types


def get_files_info(working_directory, directory=""):
    abs_working_dir = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, directory)
    dir_path = os.path.abspath(relative_path)

    if not dir_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'

    try:
        output = ""
        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            output += f"- {file_name}: file_size={file_size}, is_dir={is_dir}\n"
        return output
    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

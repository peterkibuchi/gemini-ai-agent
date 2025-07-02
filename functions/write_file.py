import os


def write_file(working_directory, file_path, content):
    working_directory = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, file_path)
    file_path = os.path.abspath(relative_path)

    if not file_path.startswith(working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.exists(file_path) and os.path.isdir(file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    if not os.path.exists(file_path):
        try:
            dir_path = os.path.dirname(file_path)
            if dir_path:  # Only create directories if there's actually a directory path
                os.makedirs(dir_path, exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"

    try:
        with open(file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error writing to file "{file_path}": {e}'

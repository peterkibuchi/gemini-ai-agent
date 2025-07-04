import os


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(relative_path)

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        MAX_CHARS = 10000
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1)

        if len(file_content_string) > MAX_CHARS:
            # There was more content, so truncate and add message
            file_content_string = file_content_string[:MAX_CHARS] + \
                f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

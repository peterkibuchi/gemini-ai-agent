import os


def get_files_info(working_directory, directory=""):
    working_directory = os.path.abspath(working_directory)
    relative_path = os.path.join(working_directory, directory)
    dir_path = os.path.abspath(relative_path)

    if not dir_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_path):
        return f'Error: "{dir_path}" is not a directory'

    try:
        result = ""
        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            result += f"- {file_name}: file_size={file_size}, is_dir={is_dir}\n"
        return result
    except Exception as e:
        return f"Error listing files: {e}"

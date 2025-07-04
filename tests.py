from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file_content import write_file
from functions.run_python import run_python_file


def test():
    # print("Calling get_files_info w/ ('calculator'):")
    # print(get_files_info("calculator"), "\n")

    # print("Calling get_files_info w/ ('calculator', '.'):")
    # print(get_files_info("calculator", "."), "\n")

    # print("Calling get_files_info w/ ('calculator', 'pkg'):")
    # print(get_files_info("calculator", "pkg"), "\n")

    # print("Calling get_files_info w/ ('calculator', '/bin'):")
    # print(get_files_info("calculator", "/bin"), "\n")

    # print("Calling get_files_info w/ ('calculator', '../'):")
    # print(get_files_info("calculator", "../"), "\n")

    # print("Calling get_file_content w/ ('calculator', 'lorem.txt'):")
    # print(get_file_content("calculator", "lorem.txt"), "\n")

    # print("Calling get_file_content w/ ('calculator', 'main.py'):")
    # print(get_file_content("calculator", "main.py"), "\n")

    # print("Calling get_file_content w/ ('calculator', 'pkg/calculator.py'):")
    # print(get_file_content("calculator", "pkg/calculator.py"), "\n")

    # print("Calling get_file_content w/ ('calculator', '/bin/cat'):")
    # print(get_file_content("calculator", "/bin/cat"), "\n")

    # print("Calling write_file w/ ('calculator', 'lorem.txt', 'wait, this isn't lorem ipsum'):")
    # print(write_file("calculator", "lorem.txt",
    #       "wait, this isn't lorem ipsum"), "\n")

    # print("Calling write_file w/ ('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet'):")
    # print(write_file("calculator", "pkg/morelorem.txt",
    #       "lorem ipsum dolor sit amet"), "\n")

    # print("Calling write_file w/ ('calculator', '/tmp/temp.txt', 'this should not be allowed'):")
    # print(write_file("calculator", "/tmp/temp.txt",
    #       "this should not be allowed"), "\n")

    print("Calling run_python_file w/ ('calculator', 'main.py'):")
    print(run_python_file("calculator", "main.py"), "\n")

    print("Calling run_python_file w/ ('calculator', 'tests.py'):")
    print(run_python_file("calculator", "tests.py"), "\n")

    print("Calling run_python_file w/ ('calculator', '../main.py'):")
    print(run_python_file("calculator", "../main.py"), "\n")

    print("Calling run_python_file w/ ('calculator', 'nonexistent.py'):")
    print(run_python_file("calculator", "nonexistent.py"), "\n")


if __name__ == "__main__":
    test()

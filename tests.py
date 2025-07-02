from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info


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

    # print("Calling get_files_info w/ ('calculator', 'lorem.txt'):")
    # print(get_file_content("calculator", "lorem.txt"), "\n")

    print("Calling get_files_info w/ ('calculator', 'main.py'):")
    print(get_file_content("calculator", "main.py"), "\n")

    print("Calling get_files_info w/ ('calculator', 'pkg/calculator.py'):")
    print(get_file_content("calculator", "pkg/calculator.py"), "\n")

    print("Calling get_files_info w/ ('calculator', '/bin/cat'):")
    print(get_file_content("calculator", "/bin/cat"), "\n")


if __name__ == "__main__":
    test()

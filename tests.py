from functions.get_files_info import get_files_info


def test():
    print("Calling get_files_info w/ ('calculator'):")
    print(get_files_info("calculator"), "\n")

    print("Calling get_files_info w/ ('calculator', '.'):")
    print(get_files_info("calculator", "."), "\n")

    print("Calling get_files_info w/ ('calculator', 'pkg'):")
    print(get_files_info("calculator", "pkg"), "\n")

    print("Calling get_files_info w/ ('calculator', '/bin'):")
    print(get_files_info("calculator", "/bin"), "\n")

    print("Calling get_files_info w/ ('calculator', '../'):")
    print(get_files_info("calculator", "../"), "\n")


if __name__ == "__main__":
    test()

import sys
import typing


def check_argv(arguments: list[str]) -> bool:
    if len(arguments) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return False
    return True


def access_file(file_name: str) -> typing.IO[str] | None:
    file: typing.IO[str]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name)
    except OSError as error:
        print(f"Error opening file '{file_name}':", error)
        return None
    return file


def read_file(file: typing.IO[str], file_name: str) -> str:
    content: str

    content = file.read()
    print("---")
    print(content, end="")
    print("---")
    file.close()
    print(f"File '{file_name}' closed.")
    return content


def transform_content(content: str) -> str:
    lines: list[str]
    new_content: str

    lines = content.splitlines()
    for i in range(len(lines)):
        lines[i] = lines[i] + "#"
    new_content = "\n".join(lines)
    return new_content


def save_newfile(new_content: str, file_name: str) -> bool:
    new_file: typing.IO[str]

    try:
        new_file = open(file_name, "w")
        new_file.write(new_content)
        new_file.close()
    except OSError as error:
        print(error)
        return False
    return True


if __name__ == "__main__":
    file: typing.IO[str] | None
    file_name: str
    new_content: str
    new_filename: str

    if check_argv(sys.argv):
        file_name = sys.argv[1]
        file = access_file(file_name)
        if file is not None:
            content = read_file(file, file_name)
            new_content = transform_content(content)
            print("Transform data:")
            print("---")
            print(new_content)
            print("---")
            new_filename = input("Enter new file name (or empty): ")
            if new_filename:
                print(f"Saving data to '{new_filename}'")
                if save_newfile(new_content, new_filename):
                    print(f"Data saved in file '{new_filename}'")
            else:
                print("Not saving data.")

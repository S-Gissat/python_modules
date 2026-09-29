import sys
import typing


def check_argv(arguments: list[str]) -> bool:
    if len(arguments) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return False
    return True


def access_file(file_name: str) -> typing.IO[str] | None:
    file: typing.IO[str]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name)
    except OSError as error:
        print(f"Error opening file '{file_name}':", error)
        return None
    return file


def read_file(file: typing.IO[str], file_name: str) -> None:
    content: str

    content = file.read()
    print("---")
    print(content, end="")
    print("---")
    file.close()
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    file: typing.IO[str] | None
    file_name: str

    if check_argv(sys.argv):
        file_name = sys.argv[1]
        file = access_file(file_name)
        if file is not None:
            read_file(file, file_name)

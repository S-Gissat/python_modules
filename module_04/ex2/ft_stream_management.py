import sys
import typing


def check_argv(arguments: list[str]) -> bool:
    if len(arguments) != 2:
        print("Usage: ft_stream_management.py <file>")
        return False
    return True


def access_file(file_name: str, arg: str) -> typing.IO[str] | None:
    file: typing.IO[str]

    try:
        file = open(file_name, arg)
    except OSError as error:
        print(f"[STDERR] Error opening file '{file_name}': {error}",
              file=sys.stderr)
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
    i: int

    i = 0
    lines = content.splitlines()
    while i < len(lines):
        lines[i] = lines[i] + "#"
        i += 1
    new_content = "\n".join(lines)
    return new_content


def save_newfile(new_content: str, file_name: str) -> bool:
    new_file: typing.IO[str] | None

    try:
        new_file = access_file(file_name, "w")
        if new_file is not None:
            new_file.write(new_content)
            new_file.close()
        else:
            print("Data not saved.")
            return False
    except OSError as error:
        print(f"[STDERR] Error writing file '{file_name}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        return False
    return True


if __name__ == "__main__":
    file: typing.IO[str] | None
    file_name: str
    new_content: str
    new_filename: str

    if check_argv(sys.argv):
        file_name = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{file_name}'")
        file = access_file(file_name, "r")
        if file is not None:
            content = read_file(file, file_name)
            new_content = transform_content(content)
            print("Transform data:")
            print("---")
            print(new_content)
            print("---")
            print("Enter new file name (or empty): ", end="")
            sys.stdout.flush()
            new_filename = sys.stdin.readline()
            new_filename = new_filename.rstrip("\n")
            if new_filename:
                print(f"Saving data to '{new_filename}'")
                if save_newfile(new_content, new_filename):
                    print(f"Data saved in file '{new_filename}'")
            else:
                print("Not saving data.")

def secure_archive(file_name: str,
                   action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    message: tuple[bool, str]

    if action == "read":
        try:
            with open(file_name, "r") as file:
                content = file.read()
        except OSError as error:
            message = (False, str(error))
            return message
        message = (True, content)
        return message
    elif action == "write":
        try:
            with open(file_name, "w") as file:
                file.write(content)
        except OSError as error:
            message = (False, str(error))
            return message
        message = (True, "Content successfully written to file")
        return message
    else:
        message = (False, "Invalid action")
        return message


if __name__ == "__main__":
    message: tuple[bool, str]

    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    message = secure_archive("/not/existing/file")
    print(message)

    print("Using 'secure_archive' to read from an inaccessible file:")
    message = secure_archive("/etc/master.passwd")
    print(message)

    print("Using 'secure_archive' to read from a regular file:")
    message = secure_archive("test_files/ancient_fragment.txt")
    print(message)

    if message[0]:
        print("Using 'secure_archive' to write "
              "previous content to a new file:")
        message = secure_archive("new_archive.txt", "write", message[1])
        print(message)

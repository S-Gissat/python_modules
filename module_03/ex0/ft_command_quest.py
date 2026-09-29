import sys

if __name__ == "__main__":
    argv_len: int
    command_len: int
    i: int

    argv_len = len(sys.argv)
    command_len = argv_len - 1
    i = 1

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if argv_len == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {command_len}")
        while i <= command_len:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {argv_len}")

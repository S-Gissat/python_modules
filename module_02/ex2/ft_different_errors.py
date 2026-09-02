def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        5 / 0
    elif operation_number == 2:
        open("./non/existent/file")
    elif operation_number == 3:
        "str" + 1


def test_error_types() -> None:

    operations: list[int]

    operations = [0, 1, 2, 3, 4]
    print("=== Garden Error Types Demo ===")
    for ops in operations:
        print(f"Testing operation {ops}...")
        try:
            garden_operations(ops)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        else:
            print("Operation completed successfully")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

def input_temperature(temp_str: str) -> int:
    temperature: int
    temperature = int(temp_str)
    if temperature > 40:
        raise ValueError(f"{temperature} is too hot for plants (max 40°C)")
    elif temperature < 0:
        raise ValueError(f"{temperature} is too cold for plants (min 0°C)")
    return temperature


def test_temperature() -> None:
    result: int
    test_data: list[str]

    test_data = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===")
    for temp in test_data:
        print(f"Input data is '{temp}'")
        try:
            result = input_temperature(temp)
            print(f"Temperature is now {result}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

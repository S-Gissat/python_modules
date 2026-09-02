class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def wilting() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_empty() -> None:
    raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    print("Testing PlantError...")
    try:
        wilting()
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    print("Testing WaterError...")
    try:
        water_empty()
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")
    try:
        wilting()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        water_empty()
    except GardenError as error:
        print(f"Caught GardenError: {error}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_errors()
    print("\nAll custom error types work correctly!")

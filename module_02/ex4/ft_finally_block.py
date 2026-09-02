class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == str.capitalize(plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    plants: list[str]
    plants2: list[str]

    plants = ["Tomato", "Lettuce", "Carrots"]
    plants2 = ["Tomato", "lettuce", "Carrots"]
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant2 in plants2:
            water_plant(plant2)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":

    print("=== Garden Watering System ===\n")

    test_watering_system()

    print("Cleanup always happens, even with errors!")

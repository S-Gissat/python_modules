class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age
        print("Plant created: ", end="")
        self.show()

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        elif height == self._height:
            print("Height unchanged")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        elif age == self._age:
            print("Age unchanged")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    plant2 = Plant("Sunflower", -10, -5)

    plant2.show()

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-8)

    plant.show()

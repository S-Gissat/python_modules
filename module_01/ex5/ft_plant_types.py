class Plant:

    def __init__(self, name: str, height: float, age: int,
                 growthratio: float = 0) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growthratio = growthratio

    def set_height(self, height: float) -> None:
        if height < 0:
            print("Error, height can't be negative")
            print("Height update rejected")
        elif height == self._height:
            print("Height unchanged")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Error, age can't be negative")
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

    def grow(self) -> None:
        if self._growthratio:
            self._height = round(self._height + self._growthratio, 2)

    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloom: bool) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom = bloom

    def bloom(self) -> None:
        self._bloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloom:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk: float, shade: dict) -> None:
        super().__init__(name, height, age)
        self._trunk = trunk
        self._shade = shade

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._shade['long']}cm"
              f" long and {self._shade['wide']}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growthratio: float, harvest_season: str) -> None:
        super().__init__(name, height, age, growthratio)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def nutrition(self) -> None:
        self._nutritional_value += 1

    def grow(self) -> None:
        super().grow()
        self.nutrition()


def get_plant_database() -> tuple[Flower, Tree, Vegetable]:
    return (
        Flower("Rose", 25.0, 30, "red", False),
        Tree("Oak", 200.0, 365, 5, shade={"long": 200, "wide": 5}),
        Vegetable("Tomato", 5.0, 10, 2.1, "April"),
    )


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    PLANT_DATABASE = get_plant_database()

    flower = PLANT_DATABASE[0]
    tree = PLANT_DATABASE[1]
    vegetable = PLANT_DATABASE[2]

    print("=== Flower")
    flower.show()
    if not flower._bloom:
        print("[asking the rose to bloom]")
        flower.bloom()
        flower.show()

    print("\n=== Tree")
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable.show()
    print(f"[make {vegetable._name} grow and age for 20 days]")
    for i in range(20):
        vegetable.grow()
        vegetable.age()
    vegetable.show()

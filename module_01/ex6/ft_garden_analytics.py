class Plant:

    def __init__(self, name: str, height: float, age: int,
                 growthratio: float) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._growthratio = growthratio
        self._stats = self.Stats()

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
        self._stats.show_called()
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._stats.grow_called()
        if self._growthratio:
            self._height = round(self._height + self._growthratio, 2)

    def age(self) -> None:
        self._stats.age_called()
        self._age += 1

    def show_stats(self) -> None:
        self._stats.show()

    @staticmethod
    def days_year(age: int) -> bool:
        if age <= 365:
            return False
        else:
            return True

    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def grow_called(self) -> None:
            self._grow_calls += 1

        def age_called(self) -> None:
            self._age_calls += 1

        def show_called(self) -> None:
            self._show_calls += 1

        def show(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

    @classmethod
    def anonym(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 growthratio: float, color: str, bloom: bool) -> None:
        super().__init__(name, height, age, growthratio)
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
                 growthratio: float, trunk: float, shade: dict) -> None:
        super().__init__(name, height, age, growthratio)
        self._trunk = trunk
        self._shade = shade
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self._name} now produces a shade of "
              f"{self._shade['long']}cm long and "
              f"{self._shade['wide']}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk}cm")

    def show_stats(self) -> None:
        super().show_stats()
        print(f"{self._shade_calls} shade")


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

    def grow(self) -> None:
        super().grow()
        self.nutrition()

    def nutrition(self) -> None:
        self._nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 growthratio: float, color: str, bloom: bool) -> None:
        super().__init__(name, height, age, growthratio, color, bloom)
        self._seeds = 0

    @classmethod
    def from_flower(cls, flower: Flower) -> "Seed":
        seed = cls(flower._name, flower._height, flower._age,
                   flower._growthratio, flower._color, flower._bloom)
        if flower._bloom:
            seed.bloom()
        return seed

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def show_stats(plant: Plant) -> None:
    plant.show_stats()


def get_plant_database() -> tuple[Flower, Tree, Flower]:
    return (
        Flower("Rose", 25.0, 30, 0.3, "red", False),
        Tree("Oak", 200.0, 365, 0.1, 5, shade={"long": 200, "wide": 5}),
        Flower("Sunflower", 80.0, 45, 0.5, "yellow", False)
    )


if __name__ == "__main__":
    print("=== Garden statistics ===")
    PLANT_DATABASE = get_plant_database()

    flower = PLANT_DATABASE[0]
    tree = PLANT_DATABASE[1]
    sunflower = PLANT_DATABASE[2]

    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.days_year(30))
    print("Is 400 days more than a year? ->", Plant.days_year(400))

    print("\n=== Flower")
    flower.show()
    show_stats(flower)
    if not flower._bloom:
        print("[asking the rose to grow and bloom]")
        flower.grow()
        flower.bloom()
        flower.show()
    show_stats(flower)

    print("\n=== Tree")
    tree.show()
    show_stats(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    show_stats(tree)

    print("\n=== Seed")
    seed = Seed.from_flower(sunflower)
    seed.show()
    show_stats(seed)
    print("[make seed grow, age and bloom]")
    seed.grow()
    seed.age()
    seed.bloom()
    seed.show()
    show_stats(seed)

    print("\n=== Anonymous")
    anonym = Plant.anonym()
    anonym.show()
    show_stats(anonym)

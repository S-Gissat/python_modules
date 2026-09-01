class Plant:
    def __init__(self, name: str, height: float, ages: int,
                 growthratio: float = 0.0) -> None:
        self.name = name
        self.height = height
        self.ages = ages
        self.growthratio = growthratio
        self.total = 0.0
        print("Created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.ages} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growthratio, 2)
        self.total = self.total + self.growthratio

    def age(self) -> None:
        self.ages += 1


def get_plant_database() -> list[Plant]:
    return [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    PLANT_DATABASE = get_plant_database()

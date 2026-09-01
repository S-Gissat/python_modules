day = 1


class Plant:
    def __init__(self, name: str, height: float, ages: int,
                 growthratio: float) -> None:
        self.name = name
        self.height = height
        self.ages = ages
        self.growthratio = growthratio
        self.total = 0.0

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.ages} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growthratio, 2)
        self.total = self.total + self.growthratio

    def age(self) -> None:
        self.ages += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Plant Growth ===")
    rose.show()
    while day <= 7:
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
        day += 1
    print(f"Growth this week: {rose.total}cm")

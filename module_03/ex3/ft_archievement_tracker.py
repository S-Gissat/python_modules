import random

ALL_ACHIEVEMENTS: list[str] = ["Crafting Genius", "Strategist", "World Savior",
                               "Speed Runner", "Sharp Mind", "Master Explorer",
                               "Treasure Hunter", "Unstoppable", "First Steps",
                               "Collector Supreme", "Untouchable", "Survivor",
                               "Boss Slayer", "Hidden Path Finder"]


def gen_player_achievements() -> set[str]:
    achievements: set[str]
    tmp_lst: list[str]
    amount: int

    amount = random.randint(4, 11)
    tmp_lst = random.sample(ALL_ACHIEVEMENTS, amount)

    achievements = set(tmp_lst)

    return achievements


if __name__ == "__main__":
    players: list[tuple[str, set[str]]]
    distinct_achievements: set[str]
    common_achievements: set[str] | None = None
    only_achievements: set[str]
    other_achievements: set[str]

    players = [("Alice", gen_player_achievements()),
               ("Bob", gen_player_achievements()),
               ("Charlie", gen_player_achievements()),
               ("Dylan", gen_player_achievements())]
    distinct_achievements = set()

    print("=== Achievement Tracker System ===")

    for name, achievements in players:
        print(f"Player {name}: {achievements}")
        distinct_achievements = distinct_achievements.union(achievements)
        if common_achievements is None:
            common_achievements = achievements
        else:
            common_achievements = common_achievements.intersection(
                achievements)

    print("All distinct achievements:", distinct_achievements)
    print("Common achievements:", common_achievements)

    for name, achievements in players:
        other_achievements = set()
        for other_name, other_set in players:
            if other_name != name:
                other_achievements = other_achievements.union(other_set)
        only_achievements = achievements.difference(other_achievements)
        print(f"Only {name} has:", only_achievements)

    for name, achievements in players:
        print(f"{name} is missing:",
              set(ALL_ACHIEVEMENTS).difference(achievements))

import random

if __name__ == "__main__":
    players: list[str]
    player_list: list[str]
    capitalized_list: list[str]
    score_list: dict[str, int]
    high_scores: dict[str, int]
    average: float

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']

    print("=== Game Data Alchemist ===")

    print("Initial list of players:", players)

    capitalized_list = [name.capitalize() for name in players]
    print("New list with all names capitalized:", capitalized_list)

    player_list = [name for name in players if name[0] == name[0].capitalize()]
    print("New list of capitalized names only:", player_list)

    score_list = {name: random.randint(0, 1000) for name in capitalized_list}
    print("Score dict:", score_list)

    average = round(sum(score_list.values()) / len(score_list), 2)
    print("Score average is", average)

    high_scores = {name: score_list[name]
                   for name in score_list
                   if score_list[name] > average}
    print("High scores:", high_scores)

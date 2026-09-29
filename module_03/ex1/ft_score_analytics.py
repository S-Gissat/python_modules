import sys

def test_commands(argv_command: list[str], command_len: int) -> list[int]:
    scores: list[int]
    i: int
    tmp: int

    i = 1
    scores = []
    while i <= command_len:
        try:
            tmp = int(argv_command[i])
            scores.append(tmp)
        except ValueError:
            print(f"Invalid parameter: '{argv_command[i]}'")
        i += 1
    return scores



def print_scores(scores: list[int]) -> None:
    score_list_len: int

    score_list_len = len(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {score_list_len}")
    print("Total score:", sum(scores))
    print("Average score:", sum(scores) / score_list_len)
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))


def ft_score_analytics(argv_command: list[str]) -> None:
    scores: list[int]
    argv_len: int
    command_len: int

    scores = []
    argv_len = len(argv_command)
    command_len = argv_len - 1

    if argv_len == 1:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return
    scores = test_commands(argv_command, command_len)
    if len(scores) == 0:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print_scores(scores)


if __name__ == "__main__":
    scores: list[str]

    scores = sys.argv

    print("=== Player Score Analytics ===")
    ft_score_analytics(scores)

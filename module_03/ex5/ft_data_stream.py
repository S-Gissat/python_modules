import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    player: str
    action: str
    event: tuple[str, str]
    players: list[str] = ["Bob", "Alice", "Dylan", "Charlie"]
    actions: list[str] = ["move", "grab", "use", "climb", "run",
                          "release", "swim", "sleep", "eat"]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        event = (player, action)
        yield event


def event_list() -> list[tuple[str, str]]:
    list_generator: typing.Generator[tuple[str, str], None, None]
    event_lst: list[tuple[str, str]]

    list_generator = gen_event()
    event_lst = []
    for i in range(10):
        event_lst.append(next(list_generator))
    return event_lst


def consume_event(events: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    event: tuple[str, str]

    while len(events):
        event = random.choice(events)
        events.remove(event)
        yield event


if __name__ == "__main__":
    generator: typing.Generator[tuple[str, str], None, None]
    consume: typing.Generator[tuple[str, str], None, None]
    event: tuple[str, str]
    events: list[tuple[str, str]]

    generator = gen_event()
    print("=== Game Data Stream Processor ===")

    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    events = event_list()
    print("Built list of 10 events:", events)
    for event in consume_event(events):
        print("Got event from list:", event)
        print("Remains in list:", events)

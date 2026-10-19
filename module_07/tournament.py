from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy,
                 NormalStrategy,
                 DefensiveStrategy,
                 AggressiveStrategy,
                 InvalidStrategyError)


def tournament(
        opponents: list[tuple[
            CreatureFactory, BattleStrategy]]) -> None:
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print("* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("now fight!")
            try:
                for action in strategy1.act(creature1):
                    print(action)
                for action in strategy2.act(creature2):
                    print(action)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    opponents: list[tuple[CreatureFactory, BattleStrategy]]

    flame_factory = FlameFactory()
    healing_factory = HealingCreatureFactory()
    aqua_factory = AquaFactory()
    transform_factory = TransformCreatureFactory()
    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()
    print("Tournament 0 (basic)")
    opponents = [(flame_factory, normal),
                 (healing_factory, defensive)]
    print("*** Tournament ***")
    print("2 opponents involved")
    tournament(opponents)
    print()

    print("Tournament 1 (error)")
    opponents = [(flame_factory, aggressive),
                 (healing_factory, defensive)]
    print("*** Tournament ***")
    print("2 opponents involved")
    tournament(opponents)
    print()

    print("Tournament 2 (multiple)")
    opponents = [(aqua_factory, normal),
                 (healing_factory, defensive),
                 (transform_factory, aggressive)]
    print("*** Tournament ***")
    print("3 opponents involved")
    tournament(opponents)


if __name__ == "__main__":
    main()

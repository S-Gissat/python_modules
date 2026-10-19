from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory, evolution: str) -> None:
    if evolution == "base":
        creature = factory.create_base()
    elif evolution == "evolved":
        creature = factory.create_evolved()
    else:
        raise ValueError("Unknown evoloution level!")
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


def test_transform(factory: TransformCreatureFactory,
                   evolution: str) -> None:
    if evolution == "base":
        creature = factory.create_base()
    elif evolution == "evolved":
        creature = factory.create_evolved()
    else:
        raise ValueError("Unknown evolution level!")

    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


def main() -> None:
    print("Testing Creature with healing capability")
    healing_factory = HealingCreatureFactory()
    print("base:")
    test_healing(healing_factory, "base")
    print("evolved:")
    test_healing(healing_factory, "evolved")

    print()

    print("Testing Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    print("base:")
    test_transform(transform_factory, "base")
    print("evolved:")
    test_transform(transform_factory, "evolved")


if __name__ == "__main__":
    main()

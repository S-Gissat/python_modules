# Python Module 07 — DataDeck

## Overview

This module explores advanced object-oriented design patterns by building a modular creature card system.

The project extends concepts such as abstract classes, inheritance and polymorphism with:

- Abstract Factory Pattern
- Multiple Inheritance
- Independent Capabilities
- Strategy Pattern
- Custom Exceptions
- Type-safe polymorphic behavior

## Project Structure

```text
.
├── ex0/
│   ├── __init__.py
│   ├── creature.py
│   └── factory.py
├── ex1/
│   ├── __init__.py
│   ├── capabilities.py
│   ├── creatures.py
│   └── factory.py
├── ex2/
│   ├── __init__.py
│   ├── exceptions.py
│   └── strategy.py
├── battle.py
├── capacitor.py
└── tournament.py
```

## Exercise 0 — Creature Factory

The first exercise introduces the **Abstract Factory Pattern**.

An abstract `Creature` class defines common behavior, while concrete creatures implement their own attacks.

Creature families are created through factories:

```text
FlameFactory
├── Flameling
└── Pyrodon

AquaFactory
├── Aquabub
└── Torragon
```

The calling code only interacts with the common `CreatureFactory` interface and does not need to know which concrete creature class will be instantiated.

## Exercise 1 — Capabilities

The second exercise adds independent capabilities that do not inherit from `Creature`.

```text
HealCapability
└── heal()

TransformCapability
├── transform()
└── revert()
```

Creatures can combine these capabilities through multiple inheritance.

Healing family:

```text
Sproutling
Bloomelle
```

Transforming family:

```text
Shiftling
Morphagon
```

Transforming creatures maintain a persistent `transformed` state which changes their attack behavior.

## Exercise 2 — Battle Strategies

The final exercise implements the **Strategy Pattern**.

A `BattleStrategy` defines:

```python
is_valid()
act()
```

Three concrete strategies are available:

```text
NormalStrategy
→ attack

AggressiveStrategy
→ transform
→ attack
→ revert

DefensiveStrategy
→ attack
→ heal
```

Strategies validate whether a creature supports the required capability before executing their actions.

Invalid creature-strategy combinations raise a dedicated `InvalidStrategyError`.

## Tournament

`tournament.py` combines factories and strategies:

```python
(CreatureFactory, BattleStrategy)
```

The tournament can therefore work with different creature families without knowing their concrete implementations.

Each opponent fights every other opponent once, while its assigned strategy determines how it behaves during battle.

## Running

```bash
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

## What I Learned

This module showed how object-oriented design patterns can separate responsibilities within a program.

The Abstract Factory Pattern separates object creation from the code using the objects.

Capabilities allow behavior to be composed independently from the main inheritance hierarchy.

The Strategy Pattern moves behavioral decisions outside the creatures themselves, making the tournament logic independent of specific creature types.

The project also demonstrates how abstract interfaces, multiple inheritance, runtime type checks, custom exceptions and static type annotations can work together in a modular Python architecture.

---

Built as part of the **42 curriculum**.
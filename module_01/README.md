# Code Cultivation 🌱
### Object-Oriented Garden System in Python

A small object-oriented Python project exploring how a simple data model can
evolve into a structured and extensible system.

Starting with a basic `Plant` model, the project gradually develops a hierarchy
of specialized plant types with their own state, behavior, validation, and
statistics.

## Overview

The core of the project is a reusable `Plant` class representing shared
properties such as name, height, age, and growth behavior.

Specialized plant types extend this model through inheritance:

```text
Plant
├── Flower
│   └── Seed
├── Tree
└── Vegetable
```

Each subclass adds its own behavior while reusing functionality provided by its
parent classes.

- `Flower` adds color and blooming behavior
- `Tree` adds trunk information and shade production
- `Vegetable` tracks harvest information and nutritional development
- `Seed` extends `Flower` with seed production

## Design

The project progressively introduces object-oriented design concepts instead of
implementing every plant type independently.

Common functionality remains in `Plant`, while specialized behavior is added
through inheritance and method overriding.

For example:

```python
class Tree(Plant):
    def produce_shade(self) -> None:
        ...
```

This keeps shared logic centralized and allows specialized plant types to extend
the system without duplicating the base implementation.

Later stages introduce an internal statistics system that tracks object behavior
such as calls to `grow()`, `age()`, and `show()`.

Trees extend this with an additional counter for shade production.

## Concepts Demonstrated

- Python classes and object instances
- Constructors with `__init__`
- Object state and methods
- Encapsulation and protected attributes
- Getters and setters
- Data validation
- Inheritance
- `super()`
- Method overriding
- Polymorphic behavior
- Nested classes
- Static methods
- Class methods
- Type hints
- Code validation with `mypy` and `flake8`

## Project Progression

| Exercise | Focus |
| --- | --- |
| `ex0` | Python program structure and `__main__` |
| `ex1` | Classes and object instances |
| `ex2` | Object state, growth, and aging |
| `ex3` | Constructors and reusable object creation |
| `ex4` | Encapsulation and data validation |
| `ex5` | Inheritance and specialized plant types |
| `ex6` | Statistics, static/class methods, and deeper inheritance |

Each exercise builds on concepts introduced earlier, gradually evolving the same
garden model rather than implementing unrelated tasks.

## Example

```text
=== Garden statistics ===

=== Flower
Rose: 25.0cm, 30 days old
Color: red
Rose has not bloomed yet
Stats: 0 grow, 0 age, 1 show

=== Tree
Oak: 200.0cm, 365 days old
Trunk diameter: 5cm
Stats: 0 grow, 0 age, 1 show
0 shade
```

## Run Locally

Run an individual exercise with Python:

```bash
python3 ex6/ft_garden_analytics.py
```

## Code Quality

The project uses type hints and follows Python style requirements.

```bash
mypy ex0 ex1 ex2 ex3 ex4 ex5 ex6
flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6
```

## Repository Structure

```text
.
├── ex0/
│   └── ft_garden_intro.py
├── ex1/
│   └── ft_garden_data.py
├── ex2/
│   └── ft_plant_growth.py
├── ex3/
│   └── ft_plant_factory.py
├── ex4/
│   └── ft_garden_security.py
├── ex5/
│   └── ft_plant_types.py
├── ex6/
│   └── ft_garden_analytics.py
└── README.md
```

---

Built as part of the **42 curriculum**.
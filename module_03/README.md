# Python Module 03 — Data Quest

Mastering Python collections through lists, tuples, sets, dictionaries, generators, and comprehensions.

---

## Overview

Python Module 03 focuses on working with different collection types and choosing the appropriate data structure for a given problem.

The exercises progress from basic list manipulation and command-line arguments to more specialized structures such as tuples, sets, and dictionaries. The module then introduces generators for on-demand data processing and comprehensions for concise collection transformation and filtering.

Throughout the module, input validation, exception handling, type hints, and data analysis are combined with Python's built-in collection features.

---

## Concepts

- Lists
- Tuples
- Sets
- Dictionaries
- Command-line arguments with `sys.argv`
- Input validation
- Exception handling
- Collection iteration
- Tuple unpacking
- Set operations
- Key-value relationships
- Generators
- `yield`
- `next()`
- Lazy evaluation
- List comprehensions
- Dictionary comprehensions
- Filtering and transforming data
- Random data generation
- Type annotations
- Static type checking with `mypy`
- Code style checking with `flake8`

---

## Exercise Progression

| Exercise | Project | Main Concept |
|---|---|---|
| `ex0` | Command Quest | Command-line arguments and lists |
| `ex1` | Score Cruncher | List processing and input validation |
| `ex2` | Position Tracker | Tuples and 3D coordinates |
| `ex3` | Achievement Hunter | Sets and set operations |
| `ex4` | Inventory Master | Dictionaries and inventory analysis |
| `ex5` | Stream Wizard | Generators and data streams |
| `ex6` | Data Alchemist | List and dictionary comprehensions |

---

## Collection Progression

The module introduces Python collections step by step, with each structure solving a different kind of problem.

### Lists

Lists are introduced through command-line arguments and score processing.

They provide ordered, mutable collections that can be iterated over, extended, filtered, and analyzed.

```python
scores = [1500, 2300, 1800, 2100]
```

### Tuples

Tuples are used to represent fixed 3D coordinates.

```python
position = (1.0, 2.5, 3.0)
```

Unlike lists, tuples are immutable after creation, making them useful for structured data that should not be modified.

### Sets

Sets store unique values and make it possible to compare collections efficiently.

The achievement tracker uses:

```python
set.union()
set.intersection()
set.difference()
```

to find shared, unique, and missing achievements.

### Dictionaries

Dictionaries introduce key-value relationships.

The inventory system stores item names as keys and quantities as values.

```python
inventory = {
    "sword": 1,
    "potion": 5,
    "shield": 2
}
```

Values can then be retrieved using their corresponding keys.

```python
inventory["potion"]
```

---

## Generators

Exercise 5 introduces generators as a way to produce values only when they are needed.

A generator uses `yield` instead of returning all values at once.

```python
def generator():
    while True:
        yield value
```

Calling the generator function creates a generator object.

```python
stream = generator()
```

Values are then requested individually:

```python
value = next(stream)
```

Unlike a normal function, the generator keeps its execution state between calls. Execution continues from the previous `yield` instead of starting the function again from the beginning.

This makes generators useful for streams or large amounts of data that do not need to exist in memory at the same time.

---

## Comprehensions

Exercise 6 introduces comprehensions as a compact way to create and filter collections.

A list comprehension:

```python
[result for element in collection]
```

can replace a loop that builds a new list.

Filtering can be added directly:

```python
[element for element in collection if condition]
```

Dictionary comprehensions follow the same principle:

```python
{key: value for element in collection}
```

and can also include conditions:

```python
{key: value for element in collection if condition}
```

These expressions combine iteration, transformation, and filtering into a concise form.

---

## Repository Structure

```text
module_03/
├── ex0/
│   └── ft_command_quest.py
├── ex1/
│   └── ft_score_analytics.py
├── ex2/
│   └── ft_coordinate_system.py
├── ex3/
│   └── ft_achievement_tracker.py
├── ex4/
│   └── ft_inventory_system.py
├── ex5/
│   └── ft_data_stream.py
├── ex6/
│   └── ft_data_alchemist.py
└── README.md
```

---

## Running the Exercises

Each exercise can be executed separately with Python.

```bash
python3 ex0/ft_command_quest.py hello world 42
```

```bash
python3 ex1/ft_score_analytics.py 1500 2300 1800 2100 1950
```

```bash
python3 ex2/ft_coordinate_system.py
```

```bash
python3 ex3/ft_achievement_tracker.py
```

```bash
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2 armor:3
```

```bash
python3 ex5/ft_data_stream.py
```

```bash
python3 ex6/ft_data_alchemist.py
```

---

## Code Quality

The exercises use type annotations and are checked with both `mypy` and `flake8`.

```bash
mypy ex0 ex1 ex2 ex3 ex4 ex5 ex6
```

```bash
flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6
```

The project uses Python 3.10 or later.

---

## What I Learned

This module helped me understand that Python collections are not simply different ways of storing the same data.

Each structure has characteristics that make it useful for different problems:

- **Lists** provide ordered and mutable collections.
- **Tuples** represent fixed structured data.
- **Sets** simplify uniqueness and comparisons between collections.
- **Dictionaries** connect keys with corresponding values.
- **Generators** produce data on demand while preserving execution state.
- **Comprehensions** provide a concise way to transform and filter collections.

Coming from C, generators and comprehensions required a different way of thinking. Python often combines operations that would normally be written as several explicit steps in C into shorter expressions.

Understanding what these expressions do internally made the syntax much easier to reason about instead of treating it as Python-specific shorthand.

---

Built as part of the **42 curriculum**.
````
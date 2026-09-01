# Growing Code 🌱
### Python Fundamentals Through Garden Data

An introductory Python project from the 42 curriculum focused on the core
building blocks of the language through a series of small garden-themed
programming exercises.

The module progresses from a first output function to user input, arithmetic,
conditional logic, iteration, recursion, and typed function parameters.

## Overview

`Growing Code` introduces Python through a collection of small, independent
functions.

Each exercise focuses on one fundamental concept while using simple community
garden scenarios such as calculating plot areas, tracking harvests, checking
watering intervals, or managing seed inventories.

The emphasis is on understanding Python syntax and control flow before moving
on to larger program structures.

## Concepts Demonstrated

- Python functions
- Console output with `print()`
- User input with `input()`
- Variables and basic data types
- Type conversion
- Arithmetic operations
- Conditional statements
- Comparison operators
- `while` loops
- Recursion
- Helper functions
- Function parameters
- String methods
- Type annotations

## Exercises

| Exercise | Function | Focus |
| --- | --- | --- |
| `ex0` | `ft_hello_garden()` | Functions and basic output |
| `ex1` | `ft_garden_name()` | User input and variables |
| `ex2` | `ft_plot_area()` | Integer conversion and arithmetic |
| `ex3` | `ft_harvest_total()` | Working with multiple values |
| `ex4` | `ft_plant_age()` | Conditional logic |
| `ex5` | `ft_water_reminder()` | Comparisons and branching |
| `ex6` | `ft_count_harvest_iterative()` / `ft_count_harvest_recursive()` | Iteration and recursion |
| `ex7` | `ft_seed_inventory()` | Parameters, string handling, and type annotations |


## Testing

42 provides a small `main.py` helper for testing the exercises interactively.

```bash
python3 main.py
```

The exercise files themselves contain only the requested functions.

## Code Quality

The project targets **Python 3.10+** and follows `flake8` style requirements.

Type hints are introduced progressively and are required in the final exercise.

```bash
flake8 ex0 ex1 ex2 ex3 ex4 ex5 ex6 ex7
```

## Repository Structure

```text
module_00/
├── ex0/
│   └── ft_hello_garden.py
├── ex1/
│   └── ft_garden_name.py
├── ex2/
│   └── ft_plot_area.py
├── ex3/
│   └── ft_harvest_total.py
├── ex4/
│   └── ft_plant_age.py
├── ex5/
│   └── ft_water_reminder.py
├── ex6/
│   ├── ft_count_harvest_iterative.py
│   └── ft_count_harvest_recursive.py
├── ex7/
│   └── ft_seed_inventory.py
├── main.py
└── README.md
```

---

Built as part of the **42 curriculum**.
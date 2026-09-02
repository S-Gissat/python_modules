# Garden Guardian

> Building resilient Python programs through exception handling, custom errors, and guaranteed cleanup.

This module focuses on **error handling and defensive programming in Python** through a small smart-agriculture monitoring system.

Rather than assuming that every input, sensor reading, or operation will succeed, the exercises progressively introduce techniques for detecting failures, communicating them clearly, and allowing the program to recover without crashing.

---

## Overview

The project develops a simple garden monitoring system across five exercises.

It begins with validating potentially corrupted temperature data and gradually introduces explicit exception raising, multiple error types, custom exception hierarchies, and resource cleanup with `finally`.

The progression is:

```text
Invalid input
    ↓
Catch exceptions
    ↓
Raise exceptions intentionally
    ↓
Distinguish different failure types
    ↓
Create domain-specific exceptions
    ↓
Guarantee cleanup with finally
```

---

## Concepts

This module introduces and reinforces:

- `try` / `except`
- `raise`
- Built-in Python exceptions
- `ValueError`
- `ZeroDivisionError`
- `FileNotFoundError`
- `TypeError`
- Multiple `except` handlers
- Custom exception classes
- Exception inheritance
- `finally`
- Defensive programming
- Type hints
- Error propagation and recovery

---

## Exercise Progression

| Exercise | Project | Focus |
|----------|---------|-------|
| `ex0` | First Exception | Catching invalid input without crashing |
| `ex1` | Raise Exception | Explicitly raising exceptions for invalid data |
| `ex2` | Different Errors | Handling multiple built-in exception types |
| `ex3` | Custom Errors | Creating a domain-specific exception hierarchy |
| `ex4` | Finally Block | Guaranteed cleanup after success or failure |

---

## Exception Flow

A central concept of this module is separating the place where an error **occurs** from the place where it is **handled**.

```text
operation
    ↓
exception occurs / is raised
    ↓
normal execution stops
    ↓
Python searches for a matching except block
    ↓
exception is handled
    ↓
program can continue
```

This makes it possible for lower-level functions to report failures while higher-level code decides how the program should react.

---

## Custom Exception Hierarchy

Exercise 3 introduces application-specific exceptions:

```text
Exception
    ↑
GardenError
   ├── PlantError
   └── WaterError
```

Because `PlantError` and `WaterError` inherit from `GardenError`, they can either be handled individually or caught together through their shared parent class.

This demonstrates how exception inheritance can be used to organize related failure states in larger applications.

---

## Guaranteed Cleanup

The final exercise introduces `finally` for operations that must happen regardless of whether an error occurs.

```text
try
 │
 ├── success ──────────┐
 │                     ↓
 └── exception → except
                       ↓
                    finally
                       ↓
                    cleanup
```

In the watering system, the system is always closed — even when an invalid plant name raises an exception and the function returns early.

---

## Repository Structure

```text
module_02/
├── ex0/
│   └── ft_first_exception.py
│
├── ex1/
│   └── ft_raise_exception.py
│
├── ex2/
│   └── ft_different_errors.py
│
├── ex3/
│   └── ft_custom_errors.py
│
├── ex4/
│   └── ft_finally_block.py
│
└── README.md
```

---

## Running the Exercises

Each exercise can be executed independently:

```bash
python3 ex0/ft_first_exception.py
python3 ex1/ft_raise_exception.py
python3 ex2/ft_different_errors.py
python3 ex3/ft_custom_errors.py
python3 ex4/ft_finally_block.py
```

---

## Code Quality

The project follows the requirements of the 42 Python curriculum:

```bash
flake8 .
mypy .
```

The exercises use:

- Python 3.10+
- Type hints for functions and methods
- `flake8`-compatible formatting
- Explicit exception handling
- Small, focused functions
- Programs designed to recover from expected failures

> **Note:** Exercise 2 intentionally contains an invalid type operation in order to trigger a `TypeError`. Static type checking is expected to detect this deliberate error.

---

Built as part of the **42 curriculum**.
# Python Module 06 — The Codex

## Overview

This module focuses on Python's import system and package structure.

The exercises explore different ways to import modules and functions, how `__init__.py` can define a package interface, how relative and absolute imports work, and what happens when modules depend on each other in a circular way.

## Topics Covered

- `import module`
- `from module import function`
- Absolute and relative imports
- Nested packages
- `__init__.py`
- Package interfaces with `__all__`
- Import aliases
- Circular imports
- Avoiding circular dependencies with local imports

## Structure

```text
.
├── alchemy/
│   ├── __init__.py
│   ├── elements.py
│   ├── potions.py
│   ├── transmutation/
│   │   ├── __init__.py
│   │   └── recipes.py
│   └── grimoire/
│       ├── __init__.py
│       ├── light_spellbook.py
│       ├── light_validator.py
│       ├── dark_spellbook.py
│       └── dark_validator.py
├── elements.py
├── ft_alembic_*.py
├── ft_distillation_*.py
├── ft_transmutation_*.py
└── ft_kaboom_*.py
```

## Exercise Progression

### Alembic

Introduces different import styles and shows how functions can be exposed through a package's `__init__.py`.

### Distillation

Uses modules with identical or related dependencies and demonstrates relative imports, absolute imports and aliases.

### Transmutation

Works with nested packages and exposes functionality through multiple package levels.

### Kaboom

Demonstrates circular dependencies.

The light spellbook avoids the circular import by delaying an import until the function is executed.

The dark spellbook intentionally creates a circular dependency to demonstrate Python's partially initialized module error.

## Example

A package can expose selected functionality through `__init__.py`:

```python
from .elements import create_air
from .potions import strength_potion
from .transmutation import lead_to_gold
```

This allows the functions to be accessed directly through the package:

```python
import alchemy

alchemy.create_air()
alchemy.lead_to_gold()
```

## Running

Individual exercises can be executed with:

```bash
python3 ft_alembic_0.py
python3 ft_distillation_0.py
python3 ft_transmutation_0.py
python3 ft_kaboom_0.py
```

`ft_kaboom_1.py` is intentionally designed to fail with an `ImportError` caused by a circular dependency.

Built as part of the **42 curriculum**.
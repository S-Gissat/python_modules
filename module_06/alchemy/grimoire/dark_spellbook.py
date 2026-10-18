from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str]

    ingredients = ["bats", "frogs", "arsenic", "eyeball"]
    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    record: str
    validation: str

    validation = validate_ingredients(ingredients)
    if " - VALID" in validation:
        record = f"Spell recorded: {spell_name} ({validation})"
    elif " - INVALID" in validation:
        record = f"Spell rejected: {spell_name} ({validation})"
    else:
        raise RuntimeError("Problem with validation")

    return record

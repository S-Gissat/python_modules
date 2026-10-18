from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str]
    validated: str
    ingredients_insens: str

    allowed = light_spell_allowed_ingredients()
    ingredients_insens = ingredients.lower()
    if any(i in ingredients_insens for i in allowed):
        validated = f"{ingredients} - VALID"
    else:
        validated = f"{ingredients} - INVALID"
    return validated

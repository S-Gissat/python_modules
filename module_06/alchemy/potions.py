from . import elements as alchemy_elements
import elements as base_elements


def healing_potion() -> str:
    healing = ("Healing potion brewed with "
               f"'{alchemy_elements.create_earth()}' "
               f"and '{alchemy_elements.create_air()}'")
    return healing


def strength_potion() -> str:
    strength = ("Strength potion brewed with "
                f"'{base_elements.create_fire()}' "
                f"and '{base_elements.create_water()}'")
    return strength

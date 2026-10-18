from ..potions import strength_potion
from ..elements import create_air
import elements


def lead_to_gold() -> str:
    gold = ("Recipe transmuting Lead to Gold: "
            f"brew '{create_air()}' and '{strength_potion()}' "
            f"mixed with '{elements.create_fire()}'")
    return gold

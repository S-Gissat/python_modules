import sys


def input_inventory(arguments: list[str]) -> dict[str, int]:
    inventory: dict[str, int]
    item: str
    value: str
    quantity: int

    inventory = {}

    for i in arguments[1:]:
        try:
            item, value = i.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{i}'")
            continue
    
        try:
            quantity = int(value)
        except ValueError as error:
            print(f"Quantity error for '{item}':", error)
            continue

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
        else:
            inventory[item] = quantity
    return inventory



if __name__ == "__main__":
    inventory: dict[str, int]
    item_lst: list[str]
    total_quantity: int
    prozent: float
    most: tuple[str, int] | None = None
    least: tuple[str, int] | None = None

    print("=== Inventory System Analysis ===")

    inventory = input_inventory(sys.argv)
    print(f"Got inventory: {inventory}")

    item_lst = list(inventory.keys())
    print(f"Item list: {item_lst}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(item_lst)} items:",
          total_quantity)

    if len(inventory) > 0 and total_quantity != 0:
        for i in inventory:
            prozent = round(inventory[i] / total_quantity * 100, 1)
            print(f"Item {i} represents {prozent}%")

        for i in inventory:
            if most is None or most[1] < inventory[i]:
                most = (i, inventory[i])
            if least is None or least[1] > inventory[i]:
                least = (i, inventory[i])
        print(f"Item most abundant: {most[0]} with quantity {most[1]}")
        print(f"Item least abundant: {least[0]} with quantity {least[1]}")

    inventory.update({"magic_item": 1})
    print("Updated inventory:", inventory)

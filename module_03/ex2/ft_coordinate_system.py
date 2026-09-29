import math


def get_player_pos() -> tuple[float, float, float]:
    inp: str
    inp_list: list[str]
    tmp_lst: list[float]
    coordinates: tuple[float, float, float]
    x: str
    y: str
    z: str
    tmp: float

    while True:
        tmp_lst = []
        inp = input("Enter new coordinates as floats in format 'x,y,z':")
        inp_list = inp.split(",")
        try:
            x, y, z = inp_list
        except ValueError:
            print("Invalid syntax")
            continue

        for i in (x, y, z):
            try:
                tmp = float(i)
                tmp_lst.append(tmp)
            except ValueError as error:
                print(f"Error on parameter '{i}':", error)
                break
        else:
            coordinates = (tmp_lst[0], tmp_lst[1], tmp_lst[2])
            return coordinates


def distance_calculation(co1: tuple[float, float, float],
                         co2: tuple[float, float, float]) -> float:
    x1: float
    x2: float
    y1: float
    y2: float
    z1: float
    z2: float
    distance: float

    x1, y1, z1 = co1
    x2, y2, z2 = co2

    distance = math.sqrt(
        (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return round(distance, 4)


if __name__ == "__main__":
    co1: tuple[float, float, float]
    co2: tuple[float, float, float]
    co_center: tuple[float, float, float]
    distance: float

    co_center = 0.0, 0.0, 0.0

    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    co1 = get_player_pos()
    print("Got a first tuple:", co1)

    print(f"It includes: X={co1[0]}, Y={co1[1]}, Z={co1[2]}")
    distance = distance_calculation(co1, co_center)
    print(f"Distance to center: {distance}")

    print("Get a second set of coordinates")
    co2 = get_player_pos()
    distance = distance_calculation(co1, co2)
    print(f"Distance between the 2 sets of coordinates: {distance}")

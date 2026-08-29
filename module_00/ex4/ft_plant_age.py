def ft_plant_age():
    nbr: int
    nbr = int(input("Enter plant age in days: "))
    if nbr > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")

def ft_water_reminder():
    nbr: int
    nbr = int(input("Days since last watering: "))
    if nbr > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
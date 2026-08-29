def helper_function(days: int, day: int):
    if day <= days:
        print(f"Day {day}")
        day += 1
        helper_function(days, day)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    helper_function(days, 1)
    print("Harvest time!")
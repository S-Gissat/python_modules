def ft_count_harvest_iterative():
    nbr: int
    limit: int
    nbr = 1
    limit = int(input("Days until harvest: "))
    while nbr <= limit:
        print(f"Day {nbr}")
        nbr += 1
    print("Harvest time!")

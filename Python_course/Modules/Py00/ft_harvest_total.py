def ft_harvest_total() -> None:
    total = 0
    for i in range(1, 4):
        total = total + int(input(f"Day {i} haverst: "))
    print(f"Total harvest: {total}")
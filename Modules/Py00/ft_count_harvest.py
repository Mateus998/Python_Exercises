def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    for i in range(days):
        print(f"Day {i + 1}")
    print("Harvest time!")

def recursive_count(n: int) -> None:
    if n <= 0:
        return
    recursive_count(n-1)
    print(f"Day {n}")

def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    recursive_count(days)
    print("Harvest time!")
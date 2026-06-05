def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))
    result = "Water the plants" if days > 2 else "Plants are fine"
    print(result)
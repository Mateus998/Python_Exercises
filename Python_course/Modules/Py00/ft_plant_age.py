def ft_plant_age() -> None:
    age = int(input("Enter plant age: "))
    if age >= 60:
        print(f"Plant is ready to harvest for {age - 60} days!")
    else:
        print(f"Plant needs more time to grow. {60 - age} days")
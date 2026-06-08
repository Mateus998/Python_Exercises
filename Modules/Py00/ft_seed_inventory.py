def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit.lower() == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit.lower() == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif unit.lower() == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")

def ft_seed_inventory_dic(seed_type: str, quantity: int, unit: str) -> None:
    unit = unit.lower()
    seed_type = seed_type.capitalize()
    messages= {
        "packets" : f"{seed_type.capitalize()} seeds: {quantity} packets available",
        "area" : f"{seed_type.capitalize()} seeds: covers {quantity} square meters",
        "grams" : f"{seed_type.capitalize()} seeds: {quantity} grams total"
    }

    print(messages.get(unit, "Unknown unit type"))
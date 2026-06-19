import sys

inventory: dict[str, int] = {}

def fill_inventory():
    for arg in sys.argv[1:]:
        item = arg.split(":")
        if len(item) != 2:
            print(f"Error - Invalid parameter \"{arg}\""); continue
        if not item[0]:
            print(f"Error - Empty key \"{arg}\""); continue
        try:
            int(item[1])
        except Exception as err:
            print(err); continue
        if item[0] in inventory:
            print(f"Redundant item '{item[0]}' - discarding"); continue
        inventory.update({item[0]:int(item[1])})


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Empty inventory")
        exit()
    fill_inventory()
    print(f"Inventory -> {inventory}")
    print(f"Items -> {list(inventory.keys())}")
    total_items = sum(inventory.values())
    print(f"Total items -> {total_items}")
    for item in inventory:
        print(f"{item} -> {round(inventory[item] * 100 / total_items)}%")
    print(f"Most abundant -> {max(inventory)}: {inventory[max(inventory)]}")
    print(f"Least abundant -> {min(inventory)}: {inventory[min(inventory)]}")
    inventory.update({"new_item":1})
    print(f"Inventory -> {inventory}")
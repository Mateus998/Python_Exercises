class plant_info:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.set_height(height)
        self.set_age(age)
        self.show()

    def get_height(self) -> int:
        return self.height
    
    def get_age(self) -> int:
        return self.age
    
    def set_height(self, a: int) -> None:
        if a < 0:
            raise ValueError("Height can't be negative")
        self.height = a
        print("height updated")
    
    def set_age(self, a: int) -> None:
        if a < 0:
            raise ValueError("Age can't be negative")
        self.age = a
        print("age updated")

    def show(self):
        print(f"Current state: {self.name.capitalize()}: {round(self.get_height(), 1)}cm, {self.get_age()} days old")
    
if __name__ == "__main__":
    try:
        plant1 = plant_info("rose", 25, 30)
        plant1.set_age(5)
        plant1.set_height(-15)
        plant1.show()
    except ValueError as err:
        print(f"{err}")
    
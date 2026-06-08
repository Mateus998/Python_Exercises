class plant_info:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name.capitalize()}: {self.height}cm {self.age} days old")
    
if __name__ == "__main__":
    plant1 = plant_info("rose", 25, 30)
    plant2 = plant_info("giras", 7, 5)
    plant3 = plant_info("lemon", 1000, 699)

    plant1.show()
    plant2.show()
    plant3.show()
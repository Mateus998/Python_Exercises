class plant_info:
    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name
        self.height = height
        self.ages = age
        self.growth_rate = growth_rate

    def grow(self):
        self.height += self.growth_rate
    
    def age(self):
        self.ages += 1

    def show(self):
        print(f"{self.name.capitalize()}: {round(self.height, 1)}cm {self.ages} days old")
    
if __name__ == "__main__":
    plant1 = plant_info("rose", 25, 30, 0.3)
    plant2 = plant_info("giras", 7, 5, 0.7)
    plant3 = plant_info("lemon", 1000, 699, 0.1)

    for i in range(7):
        plant1.grow()
        plant1.age()
        plant1.show()
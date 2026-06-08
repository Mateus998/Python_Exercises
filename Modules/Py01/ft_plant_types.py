class Plant:
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
        print(f"{self.name.capitalize()}: {round(self.height, 1)}cm, {self.ages} days old")

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float, color: str):
        super().__init__(name, height, age, growth_rate)
        self.color = color

    def bloom(self):
        if self.ages > 5:
            print(f"{self.name} has bloomed")
        else:
            print(f"{self.name} has not bloomed yet")
    
    def show(self):
        super().show()
        print(f"color: {self.color}")

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float, trunk_diameter: float):
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} produce a shade of {self.height}cm long and {self.trunk_diameter}cm wide")

    def grow(self):
        self.height *= self.growth_rate
        self.trunk_diameter *= self.growth_rate

    def show(self):
        super().show()
        print(f"trunk_diameter: {self.trunk_diameter}")

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, growth_rate: float, harvest_season: str, nutricional_value: int):
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutricional_value

    def age(self):
        self.ages += 1
        self.nutritional_value *= 1.5

    def show(self):
        super().show()
        print(f"harvet_season: {self.harvest_season}, nutricional_value: {self.nutritional_value}")

if __name__ == "__main__":
    flor = Flower("rose", 10, 5, 1.1, "red")
    tree = Tree("oak", 100, 5, 1.6, 20)
    vege = Vegetable("carrot", 7, 4, 1.2, "april", 20)
    
    flor.show()
    flor.bloom()
    flor.age()
    flor.bloom()
    flor.show()

    tree.produce_shade()
    tree.grow()
    tree.produce_shade()
    tree.show()

    vege.show()
    vege.age()
    vege.show()
class Plant:
    class Statistics:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0
        
        def increment_grow(self):
            self.grow_calls += 1
        
        def increment_age(self):
            self.age_calls += 1

        def increment_show(self):
            self.show_calls += 1

        def display(self):
            print("Statistics:")
            print("Grow calls:", self.grow_calls)
            print("Age calls:", self.age_calls)
            print("Show calls:", self.show_calls)

    @staticmethod #metodo para criar funções fora da classe, nao exigem self
    def is_older_than_year(year: int):
        return year > 365
    
    @classmethod #metodo para criar funções de objetos anonimos...
    def anonymous(cls):
        return cls("Anonymous", 0, 0, 0)

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

    @classmethod
    def anonymous(cls):
        return cls("Anonymous", 0,0, 0, "black")

    def bloom(self):
        if self.ages > 5:
            print(f"{self.name} has bloomed")
        else:
            print(f"{self.name} has not bloomed yet")
    
    def show(self):
        super().show()
        print(f"color: {self.color}")
        self.Statistics.increment_show

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
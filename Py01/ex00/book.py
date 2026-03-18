from dataclasses import dataclass, field
from datetime import date
from recipe import Recipe

@dataclass
class Book:
    name: str
    last_update: date = field(init=False)
    creation_date: date = field(init=False)
    recipes_list: dict[str, list[Recipe]] = field(init=False)

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError('Empty book name')
        self.name = self.name.strip()
        self.creation_date = date.today()
        self.last_update = self.creation_date
        self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}
    
    def get_recipe_by_name(self, name: str) -> None | Recipe:
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        recipe = next((r for recipes in self.recipes_list.values() for r in recipes if r.name == name), None)
        
        if not recipe:
            print(f'Recipe {name} not found')
        else:
            print(str(recipe))
        return recipe

    def get_recipes_by_types(self, recipe_type: str) -> list[str]:
        """Get all recipe names for a given recipe_type """
        names = [recipe.name for recipe in self.recipes_list.get(recipe_type, [])]
        return names

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        try:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = date.today()
        except KeyError:
            print('Invalid recipe type to add')

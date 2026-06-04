from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    cooking_lvl: int
    cooking_time: int
    ingredients: list[str]
    description: str
    recipe_type: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError('Empty name')
        self.name = self.name.strip()
        if not (1 <= self.cooking_lvl <= 5):
            raise ValueError('Cooking_lvl out of range (1 - 5)')
        if self.cooking_time < 0:
            raise ValueError('Negative cooking_time')
        if not self.ingredients:
            raise ValueError('Empty ingredients list')
        if any(not i.strip() for i in self.ingredients):
            raise ValueError('Empty ingredient of list')
        if self.recipe_type not in {'starter', 'lunch', 'dessert'}:
            raise ValueError('recipe_type can only be starter, lunch or dessert')
        
    def __str__(self):
        """Return the string to print with the recipe info"""
        lines = [
            f'Recipe name: {self.name}',
            f'Cooking level: {self.cooking_lvl}',
            f'Cooking time: {self.cooking_time}',
            f'Ingredients: {', '.join(self.ingredients)}',
            f'Description: {self.description}',
            f'Recipe type: {self.recipe_type}'
        ]
        txt = '\n'.join(lines)
        return txt

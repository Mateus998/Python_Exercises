from recipe import Recipe
from book import Book

def main():
    try:
        rep1 = Recipe('sandes de queijo', 1, 2, ['pao', 'queijo'], 'sandes de pao e queijo', 'starter')
        # print(str(rep1))
        book1 = Book('lanches')
        print('recipes name by type')
        print(", ".join(book1.get_recipes_by_types('starter')))
        book1.add_recipe(rep1)
        book1.get_recipe_by_name('sandes de queijo')
    except ValueError as e:
        print(e)
        return
    
if __name__ == '__main__':
    main()
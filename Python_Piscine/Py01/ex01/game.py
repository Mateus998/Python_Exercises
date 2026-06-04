class GotCharacter:
    def __init__(self, first_name: str | None, is_alive: bool) -> None:
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    '''A class that represents the Stark family'''
    def __init__(self, first_name: str | None = None, is_alive: bool=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self) -> None:
        print(self.house_words)

    def die(self) -> None:
        self.is_alive = False
    
arya = Stark("Arya")
print(arya.__doc__)
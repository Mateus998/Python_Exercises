class GardenError(Exception):
    def __init__(self, message: str="Unknown garden error") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str="Unknown plant error") -> None:
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str="Unknown water error") -> None:
        super().__init__(message)

def water_plant(plant_name: str) ->None:
    if plant_name.istitle():
        print(f"{plant_name} was watered")
    else:
        raise PlantError(f"{plant_name} is not capitalized")

def test_watering_system():
    print("Water system start")
    try:
        water_plant("Rose")
        water_plant("oak")
        water_plant("Carrot")
    except PlantError as err:
        print(err); return
    finally:
        print("Water system end")

if __name__ == "__main__":
    test_watering_system()
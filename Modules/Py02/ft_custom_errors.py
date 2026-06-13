class GardenError(Exception):
    def __init__(self, message: str="Unknown garden error") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str="Unknown plant error") -> None:
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str="Unknown water error") -> None:
        super().__init__(message)

def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            raise GardenError("GardenError detected")
        case 1:
            raise PlantError("PlantError detected")
        case 2:
            raise WaterError("WaterError detected")
        case 3:
            raise GardenError()
        case 4:
            raise PlantError()
        case 5:
            raise WaterError()
        case _:
            return
        
if __name__ == "__main__":
    for i in range(6):
        try:
            garden_operations(i)
        except GardenError as err:
            print(err)
        
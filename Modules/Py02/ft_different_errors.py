def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            print(f"{10 / 0}")
        case 2:
            open("not exist")
        case 3:
            var = "str" + 1
        case _:
            return
        
if __name__ == "__main__":
    for i in range(5):
        try:
            garden_operations(i)
        except ValueError as err:
            print(f"{err}: int(\"abc\")")
        except ZeroDivisionError as err:
            print(f"{err}: 10 / 0")
        except FileNotFoundError as err:
            print(f"{err}: open(\"not exist\")")
        except TypeError as err:
            print(f"{err}: \"str\" + 1")
        except Exception as err:
            print("Generic error")
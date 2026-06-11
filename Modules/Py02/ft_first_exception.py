def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print(f"temperature: {input_temperature("25")}º")
    try:
        print(f"temperature: {input_temperature("abc")}º")
    except ValueError as err:
        print(err)
    print("end program")

if __name__ == "__main__":
    test_temperature()
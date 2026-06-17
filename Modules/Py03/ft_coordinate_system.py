import math

def get_player_pos() -> tuple[float,...]:
    input_str = input("Insert coordinates: x y z ")
    if len(input_str.split()) != 3:
        raise ValueError("Only 3 coordinates: x y z")
    coordinates = tuple(float(x) for x in input_str.split())
    return coordinates

def dist(c1: tuple[float,...], c2: tuple[float,...]) -> float:
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

if __name__ == "__main__":
    print("First set of coordinates:")
    p1 = ()
    while True :
        try:
            p1 = get_player_pos()
            break
        except ValueError as err:
            print(err)
    
    print(f"Tuple: {p1}\nx: {p1[0]}, y: {p1[1]}, z: {p1[2]}")
    print(f"Distance from center: {dist(p1,(0, 0, 0))}")

    print("Second set of coordinates:")
    p2 = ()
    while True :
        try:
            p2 = get_player_pos()
            break
        except ValueError as err:
            print(err)
    
    print(f"Tuple: {p2}\nx: {p2[0]}, y: {p2[1]}, z: {p2[2]}")
    print(f"Distance from coodinates: {dist(p1,p2)}")
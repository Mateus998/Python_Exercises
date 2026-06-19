import random

names: list[str] = ["player1", "Player2", "player3", "Player4", "player5", "Player6", "player7", "Player8", "player9", "Player10", "player11", "Player12"]

if __name__ == "__main__":
    full_cap = [i.capitalize() for i in names]
    print(full_cap)
    cap_only = [i for i in names if i.istitle()]
    print(cap_only)

    dic1 = {name:random.randint(1, 15) * 1000 for name in full_cap}
    print(dic1)
    avg = round(sum(dic1.values()) / len(dic1))
    print(avg)
    dic2 = {key:value for key, value in dic1.items() if value > avg}
    print(dic2)
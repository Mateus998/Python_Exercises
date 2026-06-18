import random

achievements = {"a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13"}

def gen_player_achievements() -> set[str]:
    quantity = random.randint(2, len(achievements) - 1)
    return set(random.sample(list(achievements), quantity))

if __name__ == "__main__":
    p1 = gen_player_achievements()
    p2 = gen_player_achievements()
    p3 = gen_player_achievements()
    p4 = gen_player_achievements()

    print(f"players achievements: {p1.union(p2, p3, p4)}")

    print(f"common achievements: {p1.intersection(p4, p2, p3)}")

    print(f"p1 unique achievements: {p1.difference(p2, p3, p4)}")
    print(f"p2 unique achievements: {p2.difference(p1, p3, p4)}")
    print(f"p3 unique achievements: {p3.difference(p1, p2, p4)}")
    print(f"p4 unique achievements: {p4.difference(p1, p3, p2)}")

    print(f"p1 missing achievements: {achievements.difference(p1)}")
    print(f"p2 missing achievements: {achievements.difference(p2)}")
    print(f"p3 missing achievements: {achievements.difference(p3)}")
    print(f"p4 missing achievements: {achievements.difference(p4)}")
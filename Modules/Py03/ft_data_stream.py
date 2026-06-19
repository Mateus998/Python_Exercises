from typing import Generator
import random

events = ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e12", "e13", "e14", "e15"]
players = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11", "p12", "p13", "p14", "p15"]

def gen_event() -> Generator[tuple[str, str], None, None]:
    name = random.choice(players)
    event = random.choice(events)
    yield (name, event)

def consume_event(lst: list[tuple[str,str]]) -> Generator[tuple[str, str], None, None]:
    while lst:
        item = random.choice(lst)
        lst.remove(item)
        yield item

if __name__ == "__main__":
    print("\n".join(f"{i} -> {next(gen_event())}" for i in range(1, 6)))
    lst: list[tuple[str, str]] = [next(gen_event()) for _ in range(5)]
    print("\n".join(f"{event}" for event in consume_event(lst)))
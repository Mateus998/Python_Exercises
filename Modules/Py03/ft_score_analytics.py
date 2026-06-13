import sys

def score_analytics():
    scores: list[int] = []
    for i in sys.argv[1:]:
        try:
            scores.append(int(i))
        except Exception as err:
            print(err)
    if not scores:
        print("No scores provaded!"); return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Avarage score: {sum(scores) / 2}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")

if __name__ == "__main__":
    score_analytics()
pick_score = {"X": 1, "Y": 2, "Z": 3}
values = {"A": 0, "X": 0, "B": 1, "Y": 1, "C": 2, "Z": 2}

def game_score(opponent, me):
    pick_diff = (values[me] - values[opponent])
    return 3 * ((pick_diff + 1) % 3)

def score(opponent, me):
    return game_score(opponent, me) + pick_score[me]

def score_with_outcome(opponent, outcome):
    if opponent == "A" and outcome == "X":
        return score(opponent, "Z")
    elif opponent == "A" and outcome == "Y":
        return score(opponent, "X")
    elif opponent == "A" and outcome == "Z":
        return score(opponent, "Y")
    elif opponent == "B" and outcome == "X":
        return score(opponent, "X")
    elif opponent == "B" and outcome == "Y":
        return score(opponent, "Y")
    elif opponent == "B" and outcome == "Z":
        return score(opponent, "Z")
    elif opponent == "C" and outcome == "X":
        return score(opponent, "Y")
    elif opponent == "C" and outcome == "Y":
        return score(opponent, "Z")
    elif opponent == "C" and outcome == "Z":
        return score(opponent, "X")

with open("Day2/input.txt", "r") as f:
    lines = f.readlines()

score1 = 0
score2 = 0
for line in lines:
    picks = line.split()
    opponents_pick = picks[0]
    my_pick = picks[1]
    expected_outcome = picks[1]
    score1 += score(opponents_pick, my_pick)
    score2 += score_with_outcome(opponents_pick, expected_outcome)
print(f"Total score: {score1}")
print(f"Second score: {score2}")
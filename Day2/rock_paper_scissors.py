pick_score = {"X": 1, "Y": 2, "Z": 3}

def game_score(opponent, me):
    if opponent == "A" and me == "X" or opponent == "B" and me == "Y" or opponent == "C" and me == "Z":
        return 3
    elif opponent == "A" and me == "Y" or opponent == "B" and me == "Z" or opponent == "C" and me == "X":
        return 6
    else:
        return 0

def get_score(opponent, me):
    return game_score(opponent, me) + pick_score[me]

with open("Day2/input.txt", "r") as f:
    lines = f.readlines()

score = 0
for line in lines:
    picks = line.split()
    opponents_pick = picks[0]
    my_pick = picks[1]
    score += get_score(opponents_pick, my_pick)
print(f"Total score: {score}")
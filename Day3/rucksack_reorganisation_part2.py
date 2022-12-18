import sys

def same_item(r1, r2, r3):
    for item in r1:
        if item in r2 and item in r3:
            return item
    return ValueError()

def get_priority(item: str):
    o = ord(item)
    if o >= ord("a") and o <= ord("z"):
        return o - (ord("a") - 1)
    elif o >= ord("A") and o <= ord("Z"):
        return o - (ord("A") - 1) + 26
    else:
        raise ValueError()

input_file = f"Day3/input.txt"
if len(sys.argv) == 2:
    input_file = sys.argv[1]
rucksacks = open(input_file, "r").readlines()
print(rucksacks)

sum_prios = 0
for i in range(int(len(rucksacks) / 3)):
    # get elves
    s1 = rucksacks[3*i]
    s2 = rucksacks[3*i + 1]
    s3 = rucksacks[3*i + 2]

    item = same_item(s1, s2, s3)
    prio = get_priority(item)
    sum_prios += prio
print(sum_prios)
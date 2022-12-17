rucksacks = open("Day3/input.txt", "r").readlines()

def same_item(s1, s2):
    for item in s1:
        if item in s2:
            return item
    raise ValueError()

def get_priority(item: str):
    o = ord(item)
    if o >= ord("a") and o <= ord("z"):
        return o - (ord("a") - 1)
    elif o >= ord("A") and o <= ord("Z"):
        return o - (ord("A") - 1) + 26
    else:
        raise ValueError()

sum_prios = 0
for rucksack in rucksacks:
    # get items from each compartment
    n_items = len(rucksack)
    s1 = rucksack[:int(n_items / 2)]
    s2 = rucksack[int(n_items / 2):]
    s2 = s2.rstrip()
    item = same_item(s1, s2)
    prio = get_priority(item)
    sum_prios += prio
print(sum_prios)
with open("Day1/input.txt", "r") as f:
    line = f.readline()
    packs = []
    current_pack = []
    while line != "":
        if line == "\n":
            packs.append(current_pack)
            current_pack = []
        else:
            current_pack.append(int(line))
        line = f.readline()
    packs.append(current_pack)

sol1 = max(map(sum, packs))
print(f"Most calories by any elf: {sol1}")
sol2 = sum(sorted(list(map(sum, packs)))[-3:])
print(f"Calories carried by top three elves: {sol2}")
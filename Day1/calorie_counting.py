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

sol = max(map(sum, packs))
print(f"Most calories by any elf: {sol}")
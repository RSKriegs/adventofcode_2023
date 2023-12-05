import re

with open("data/input_5.txt", "r") as file:
    seeds = maps = []

    for line in (r.strip() for r in file.readlines()):
        if line.startswith("seeds:"):
            seeds = [int(x) for x in line[7:].split()]
        elif re.match(r'^[^-]+-to-[^-]+\s', line):
            maps.append([])
        elif line:
            a, b, c = (int(x) for x in line.split())
            maps[-1].append([b, a, c]) #changing destination with source for intuitive convenience

#part 1
first_list = []
for seed in seeds:
    for map in maps:
        for list in map:
            if list[0] <= seed < list[0] + list[2]:
                seed = (seed - list[0]) + list[1]
                break
    first_list.append(seed)

print(min(first_list))


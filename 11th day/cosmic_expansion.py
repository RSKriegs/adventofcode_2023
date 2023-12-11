from itertools import combinations

def transform_galaxies(cosmos):
    def expand_galaxies(cosmos):
        global counter
        if counter > 1:
            return cosmos
        print(cosmos)
        final_cosmos = []
        cosmos = [list(x) for x in list(map(list, zip(*cosmos)))]
        for sublist in cosmos:
            final_cosmos.append(sublist)
            if '#' not in sublist:
                final_cosmos.append(sublist)
        counter += 1
        return expand_galaxies(final_cosmos)

    cosmos = [x for x in map(lambda x: list(x), cosmos)]
    cosmos = expand_galaxies(cosmos)

    galaxies = []
    for x in range(0, len(cosmos)):
        for y in range(0, len(cosmos[x])):
            if cosmos[x][y] == "#":
                galaxies.append((x,y))
    return galaxies

def manhattan_distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))

if __name__ == "__main__":
    with open("data/input_11.txt", "r") as file:
        items = file.read().rstrip().split('\n')
    
    counter = 0
    galaxies = transform_galaxies(items)

    combos = list(combinations(galaxies, 2))
    s = sum([manhattan_distance(combo[0], combo[1]) for combo in combos])

    print(s)
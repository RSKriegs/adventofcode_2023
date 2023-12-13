import sys
from functools import lru_cache
from itertools import dropwhile

sys.setrecursionlimit(99999999)

#to be fair I still don't exactly understand how I got it to work but I got it working
@lru_cache
def find_arrangements(springs, groups):
    if len(springs) == len(groups) == 0:
        return 1
    elif len(springs) == 0 and len(groups) != 0:
        return 0
    elif springs[0] == ".":
        return find_arrangements(tuple(dropwhile(lambda x: x == ".", springs)), groups)
    elif springs[0] == "?":
        return find_arrangements(tuple("#") + springs[1:], groups) + find_arrangements(tuple(".") + springs[1:], groups)
    elif springs[0] == "#":
        if len(groups) == 0 or len(springs) < groups[0]\
            or (springs + tuple('.'))[groups[0]] == "#"\
            or "." in springs[0:groups[0]]:
            return 0
        
        if len(springs) <= groups[0] and (springs + tuple('.'))[groups[0]] != "?":
            return find_arrangements(tuple(dropwhile(lambda x: x == ".", springs[groups[0]:])), groups[1:])
        else:
            return find_arrangements(tuple(dropwhile(lambda x: x == ".", springs[groups[0] + 1:])), groups[1:])
    else:
        return 0

if __name__=="__main__":

    with open("data/input_12.txt", "r") as file:
        items = file.read().rstrip().split('\n')

    #part 1
    springs = [(list(item.split(' ')[0]),list(map(lambda x: int(x), item.split(' ')[1].split(',')))) for item in items]
    counter = 0

    for i in range(0, len(springs)):
        result = find_arrangements(tuple(springs[i][0]), tuple(springs[i][1]))
        counter += result

    print(counter)

    #part 2
    new_springs = []
    for i in range(0, len(springs)):
        x_to_append = list()
        x_to_append.extend(springs[i][0])
        y_to_append = list()
        y_to_append.extend(springs[i][1])
        for j in range(1, 5):
            x_to_append.extend(["?"] + springs[i][0])
            y_to_append.extend(springs[i][1])
        new_springs.append((x_to_append,y_to_append))

    counter = 0
    
    for i in range(0, len(new_springs)):
        result = find_arrangements(tuple(new_springs[i][0]), tuple(new_springs[i][1]))
        counter += result

    print(counter)
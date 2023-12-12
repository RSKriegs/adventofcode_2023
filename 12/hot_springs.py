import sys
from functools import lru_cache
from itertools import dropwhile

sys.setrecursionlimit(99999999)

@lru_cache
def find_arrangements(springs, groups, temp = "", visited = ()):
    global counter
    if len(springs) == 0:
        if len(groups) == 0 or (len(groups) == 1 and groups[0] == 0):
            counter += 1
            visited = visited + tuple(temp)
        return True
    elif len(groups) == 0:
        if len(springs) == 0 or "#" not in springs:
            counter += 1
            visited = visited + tuple(temp + "." * len(springs))
        return True
    
    if springs[0] == "?":
        find_arrangements(tuple("#") + springs[1:], groups, temp, visited)
        find_arrangements(tuple(".") + springs[1:], groups, temp, visited)

    if springs[0] == "#" and groups[0] != 0:
        return find_arrangements(springs[1:], tuple([groups[0] - 1] + list(groups[1:])), temp + "#", visited)
    
    if springs[0] == "." and groups[0] == 0:
        return find_arrangements(springs[1:], groups[1:], temp + ".", visited)
    
    if springs[0] == "." and (temp == '' or temp[-1] != "#"):
        return find_arrangements(springs[1:], groups, temp + ".", visited)

#part 2
@lru_cache
def find_arrangements_2(springs, groups):
    if len(springs) == len(groups) == 0:
        return 1
    elif len(springs) == 0 and len(groups) != 0:
        return 0

    if springs[0] == "#":
        if len(groups) == 0 or len(springs) < groups[0]:
            return 0
        if (springs[groups[0]:] or [None]) == "#":
            return 0
        if "." in springs[0:groups[0]]:
            return 0
        
        if len(springs) <= groups[0]:
            if (springs[groups[0]:] or [None]) != "?":
                return find_arrangements_2(tuple(dropwhile(lambda x: x == ".", springs[groups[0]:])), groups[1:])
        else:
            return find_arrangements_2(tuple(dropwhile(lambda x: x == ".", springs[groups[0] + 1:])), groups[1:])
    elif springs[0] == ".":
        return find_arrangements_2(tuple(dropwhile(lambda x: x == ".", springs)), groups)
    elif springs[0] == "?":
        return find_arrangements_2(tuple("#") + springs[1:], groups) + find_arrangements_2(tuple(".") + springs[1:], groups)

if __name__=="__main__":

    with open("data/test.txt", "r") as file:
        items = file.read().rstrip().split('\n')

    #part 1
    springs = [(list(item.split(' ')[0]),list(map(lambda x: int(x), item.split(' ')[1].split(',')))) for item in items]
    counter = 0

    for i in range(0, len(springs)):
        find_arrangements(tuple(springs[i][0]), tuple(springs[i][1]))

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

    # TODO: 3rd and 6th example fix
    counter = 0
    
    for i in range(5, 6):
        result = find_arrangements_2(tuple(new_springs[i][0]), tuple(new_springs[i][1]))
        counter += result

    print(counter)
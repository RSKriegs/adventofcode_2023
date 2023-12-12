from functools import lru_cache

@lru_cache()
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

if __name__=="__main__":

    with open("data/input_12.txt", "r") as file:
        items = file.read().rstrip().split('\n')

    springs = [(list(item.split(' ')[0]),list(map(lambda x: int(x), item.split(' ')[1].split(',')))) for item in items]
    counter = 0

    for i in range(0, len(springs)):
        find_arrangements(tuple(springs[i][0]), tuple(springs[i][1]))

    print(counter)
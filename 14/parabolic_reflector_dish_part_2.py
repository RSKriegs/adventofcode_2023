from copy import deepcopy

def tilt_beams(beams):
    temp = [0] * len(beams[0])
    for i in range(len(beams)):
        for j in range(len(beams[0])):
            if beams[i][j] == "O":
                temp[j] += 1
                beams[i][j] = "."
                beams[temp[j] - 1][j] = "O"
            if beams[i][j] == "#":
                temp[j] = i + 1

def get_result(items):
    result = 0
    for item in items:
        for i in range(0, len(item)):
            if item[i] == 'O':
                result += len(item) - i
    return result

def calculate(beams):
    for _ in range(3):
        tilt_beams(beams)
        temp = []
        for i in range(len(beams[0])):
            temp.append(list(map(lambda x: x[i],beams))[::-1])
        beams = temp
    memory = [deepcopy(beams)]
    max = 999999999
    for cycle in range(1, max):
        for _ in range(4):
            tilt_beams(beams)
            temp = []
            for i in range(len(beams[0])):
                temp.append(list(map(lambda x: x[i],beams))[::-1])
            beams = temp
        if beams not in memory:
            memory.append(deepcopy(beams))
            continue
        return get_result(memory[memory.index(beams) + (max - cycle) % (cycle - memory.index(beams))])
    return get_result(beams)

if __name__=="__main__":

    with open("data/input_14.txt", "r") as file:
        items = file.read().rstrip().split('\n')
    beams = []

    for item in items:
        beams.append([x for x in item])
    print(calculate(beams))
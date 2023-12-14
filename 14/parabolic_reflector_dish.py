def tilt_beams(items):
    items = list(map(list, zip(*items)))
    for item in items:
        i = j = 0
        while i < len(item):
            while item[i] == '.':
                j += 1
                if j > len(item) - 1 or item[j] == '#':
                    j = i
                    break
                if item[j] == 'O':
                    item[i] = item[j]
                    item[j] = '.'
                    j = i
                    break
            i += 1
            j += 1
    return items

def get_result(items):
    result = 0
    for item in items:
        for i in range(0, len(item)):
            if item[i] == 'O':
                result += len(item) - i
    return result

if __name__=="__main__":

    with open("data/test.txt", "r") as file:
        items = file.read().rstrip().split('\n')
    #part 1
    beams = tilt_beams(items)
    print(get_result(beams))

    #couldn't solve part 2 with this approach so I've moved it to separate file
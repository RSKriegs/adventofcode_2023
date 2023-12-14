if __name__=="__main__":

    with open("data/input_14.txt", "r") as file:
        items = file.read().rstrip().split('\n')
    
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

    result = 0
    for item in items:
        for i in range(0, len(item)):
            if item[i] == 'O':
                result += len(item) - i
    print(result)
        
def find_reflections(pattern):
    result = 0
    max_counter = 0
    for i in range(0, len(pattern) - 1):
        for j in range(len(pattern) - 1, i, -1):
            if pattern[j] == pattern[i]:
                if j - 1 == i:
                    print(i, j)
                    counter = 0
                    if result == 0 and i == 0 and j == 1:
                        result = j
                    for k in range(i, 0, -1):
                        print(i, j, k, counter)
                        if pattern[k] != pattern[(j - i) + k]:
                            max_counter = max(counter, max_counter)
                            break
                        if counter < (j - i) + k:
                            if counter >= max_counter:
                                result = j
                            counter += 1
    return result

if __name__=="__main__":

    with open("data/input_13.txt", "r") as file:
        items = file.read().rstrip().split('\n')
    
    patterns = []
    temp = []
    for i in range(len(items)):
        if i == len(items) - 1:
            patterns.append(temp)
        if len(items[i]) == 0:
            patterns.append(temp)
            temp = []
        else:
            temp.append(list(items[i]))
    
    results = []
    for pattern in patterns[0:4]:
        temp_1 = find_reflections(pattern)
        temp_2 = find_reflections(list(map(list, zip(*pattern))))
        results.append(temp_1*100+temp_2)
    print(results)
#This task is rather easy by design but I found its description incomprehensible. It doesn't include any sort of description how to handle multiple reflections
#which happened to my input. I've wasted a lot of time due to that. I've managed to make it work on this input but not guarantee it will work on anyone's else.

def find_reflections(pattern):
    result = 0
    max_counter = 0
    for i in range(0, len(pattern) - 1):
        for j in range(len(pattern) - 1, i, -1):
            if pattern[j] == pattern[i]:
                if j - 1 == i:
                    counter = 0
                    if result == 0 and i == 0 and j == 1:
                        result = j
                    for k in range(i, -1, -1):
                        if j + (i - k) >= len(pattern):
                            counter += 1
                            if counter >= max_counter:
                                max_counter = max(counter, max_counter)
                                result = j
                            break
                        if pattern[k] != pattern[j + (i - k)]:
                            break
                        if k == 0:
                            counter += 1
                            if counter >= max_counter:
                                max_counter = max(counter, max_counter)
                                result = j
                            break
                        counter += 1
    return result

#I've decided to simplify the solution for the 2nd part in order to implement smudge checks
def find_reflections_2(pattern):
    for i in range(len(pattern)):
        smudges = 0
        for j in range(i + 1):
            if j + i + 1 >= len(pattern):
                break

            temp_1 = pattern[i - j]
            temp_2 = pattern[i + j + 1]
            for x, y in zip(temp_1, temp_2):
                if x != y:
                    smudges += 1
        if smudges == 1:
            return i + 1
    return 0

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
    
    #part 1
    results = []
    for pattern in patterns:
        temp_1 = find_reflections(pattern)
        temp_2 = find_reflections(list(map(list, zip(*pattern))))
        if temp_2 > temp_1:
            results.append(temp_2)
        else:
            results.append(100*temp_1)
    print(sum(results))

    #part 2
    results = []
    for pattern in patterns:
        temp_1 = find_reflections_2(pattern)
        temp_2 = find_reflections_2(list(map(list, zip(*pattern))))
        results.append(100*temp_1 + temp_2)
    print(sum(results))

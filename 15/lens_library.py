from collections import defaultdict

def hash_item(item):
    temp = 0
    for string in item:
        temp = (temp + ord(string)) * 17 % 256
    return temp

def calculate(items):
    def assign_arguments(item): #label, length, operation
        return (item[:-1], None, '-') if item[-1] == '-' else (item[:-2], int(item[-1]), '=')
    items = map(assign_arguments, items)
    boxes = defaultdict(dict)
    for item in items:
        hash = hash_item(item[0])
        if item[2] == '-':
            if item[0] in boxes[hash]:
                del boxes[hash][item[0]]
        elif item[2] == '=':
            boxes[hash][item[0]] = item[1]
    focusing_power = 0
    for i, box in boxes.items():
        for j, k in enumerate(box.values()):
            focusing_power += (i + 1) * (j + 1) * k
    return focusing_power

if __name__=="__main__":

    with open("data/input_15.txt", "r") as file:
        items = file.read().rstrip().split(',')
    
    #part 1
    print(sum(hash_item(item) for item in items))

    #part 2
    print(calculate(items))
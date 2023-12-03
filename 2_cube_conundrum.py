#day 2
with open("", "r") as file:
    items = file.read().split('\n')

list_of_dicts = []
for item in items[:-1]: #skip the last empty one
    temp = item.replace(';',',').split(": ")
    list_of_dicts.append({temp[0] : temp[1].split(', ')})

#1st question
result_1 = 0
n = 1
for item_dict in list_of_dicts:
    to_add = True
    for item in item_dict[f'Game {n}']:
        item = item.split(' ')
        if  (item[1] == 'red' and int(item[0]) > 12) or\
            (item[1] == 'green' and int(item[0]) > 13) or\
            (item[1] == 'blue' and int(item[0]) > 14):
            to_add = False
            break
    if to_add:
        result_1 += n
    n += 1
print(result_1)

#2nd question
result_2 = 0
n = 1
for item_dict in list_of_dicts:
    max_dict = {'green': None, 'red': None, 'blue': None}
    for item in item_dict[f'Game {n}']:
        item = item.split(' ')
        if max_dict[item[1]] is None or int(item[0]) > max_dict[item[1]]:
            max_dict[item[1]] = int(item[0])
    power = 1
    for value in max_dict.values():
        power *= value
    result_2 += power
    n += 1

print(result_2)
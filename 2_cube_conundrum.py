#day 2
with open("", "r") as file:
    items = file.read().split('\n')

list_of_dicts = []
for item in items[:-1]: #skip the last empty one
    temp = item.replace(';',',').split(": ")
    list_of_dicts.append({temp[0] : temp[1].split(', ')})

result = 0
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
        result += n
    n += 1
print(result)
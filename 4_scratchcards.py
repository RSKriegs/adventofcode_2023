#day 4
with open("", "r") as file:
    items = file.read().rstrip().split('\n')

list_of_dicts = []
for item in items:
    item = item.replace('|',':').split(": ")
    list_of_dicts.append({'Card' : list(filter(None,item[1].split(' '))), 
                          'Card own' : list(filter(None,item[2].split(' ')))})

#part 1
result = 0
for item_dict in list_of_dicts:
    n = 0
    for item in item_dict['Card own']:
        if item in item_dict['Card']:
            if n == 0:
                n += 1
            else:
                n *= 2
    result += n
print(result)


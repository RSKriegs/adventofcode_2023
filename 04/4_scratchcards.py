#day 4
with open("", "r") as file:
    items = file.read().rstrip().split('\n')

list_of_dicts = []
m = 1
for item in items:
    temp = item.replace('|',':').split(": ")
    list_of_dicts.append({'Card' : list(filter(None,temp[1].split(' '))), 
                          'Card own' : list(filter(None,temp[2].split(' ')))})
    m += 1

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

#part 2

second_list = [0] * (len(list_of_dicts) + 1)
for i, item_dict in enumerate(list_of_dicts):
    cards, cards_own = item_dict['Card'], item_dict['Card own']

    count = 0
    for item in item_dict['Card own']:
        if item in item_dict['Card']:
            count += 1

    if count > 0:
        for j in range(i + 2, i + count + 2):
            second_list[j] += second_list[i + 1] + 1

second_list = [num + 1 for num in second_list][1:]

print(sum(second_list))


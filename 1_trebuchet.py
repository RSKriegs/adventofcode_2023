#day 1

with open(" ", "r") as file:
    items = file.read().replace('\n', ' ').split(" ") 

final_list = []
for item in items:
    item = list(filter(lambda x: x.isdigit(), list(item)))
    if item:
        final_list.append(int(str(f'{item[0]}{item[-1]}')))

print(sum(final_list))
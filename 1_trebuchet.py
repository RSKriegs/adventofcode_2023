#day 1
import re

with open("data/input_1.txt", "r") as file:
    items = file.read().replace('\n', ' ').split(" ")

numbers = {
    "one": 'o1e',
    "two": 't2o',
    "three": 'th3ee',
    "four": 'f4ur',
    "five": 'f5ve',
    "six": 's6x',
    "seven": 'se7en',
    "eight": 'ei8ht',
    "nine": 'n9ne'
}

final_list = []
for item in items:
    temp = ''
    for x in list(item):
        temp += x
        for k, v in numbers.items():
            if k in temp:
                temp = temp.replace(k,v)
        item = temp
    item = list(filter(lambda x: x.isdigit(), list(item)))
    if item:
        final_list.append(int(str(f'{item[0]}{item[-1]}')))

print(sum(final_list))
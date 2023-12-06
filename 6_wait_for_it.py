from functools import reduce

def calculate(time, distance):
    speed = 0
    list_of_times = []
    temp = int(time)
    while speed < int(time) - 1:
        temp -= 1
        speed += 1
        if speed * temp > int(distance):
            list_of_times.append(speed * temp)
    return len(list_of_times)

with open("", "r") as file:
    items = file.read().rstrip().split('\n')

times     = items[0].split(':')[1].split()
distances = items[1].split(':')[1].split()

#1st part
final_list = []
for i in range(0, len(times)):
    final_list.append(calculate(times[i], distances[i]))

result = reduce((lambda x, y: x * y), final_list)
print(result)

#2nd part
times       = reduce((lambda x, y: f'{x}{y}'), times)
distances   = reduce((lambda x, y: f'{x}{y}'), distances)
print(calculate(times, distances))
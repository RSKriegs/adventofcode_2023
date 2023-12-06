from functools import reduce

with open("", "r") as file:
    items = file.read().rstrip().split('\n')

times     = items[0].split(':')[1].split()
distances = items[1].split(':')[1].split()

final_list = []
for i in range(0, len(times)):
    speed = 0
    list_of_times = []
    temp = int(times[i])
    while speed < int(times[i]) - 1:
        temp -= 1
        speed += 1
        if speed * temp > int(distances[i]):
            list_of_times.append(speed * temp)
    final_list.append(len(list_of_times))

result = reduce((lambda x, y: x * y), final_list)
print(result)
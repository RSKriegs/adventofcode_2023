import re

def calculate(seeds, maps):
    first_list = []
    for seed in seeds:
        for map in maps:
            for list in map:
                if list[0] <= seed < list[0] + list[2]:
                    seed = (seed - list[0]) + list[1]
                    break
        first_list.append(seed)
    return min(first_list)

def create_seeds_from_range(range_0, range_1):
    seeds_2 = []
    temp = []
    for i in range(range_0, int(round(range_1/2))):
        temp.append(i)
    seeds_2.append(temp)
    temp = []
    for i in range(int(round(range_1/2)/2), range_1):
        temp.append(i)
    seeds_2.append(temp)
    temp = []
    return(seeds_2)

if __name__ == '__main__':

    with open("data/input_5.txt", "r") as file:
        seeds = maps = []

        for line in (r.strip() for r in file.readlines()):
            if line.startswith("seeds:"):
                seeds = [int(x) for x in line[7:].split()]
            elif re.match(r'^[^-]+-to-[^-]+\s', line):
                maps.append([])
            elif line:
                a, b, c = (int(x) for x in line.split())
                maps[-1].append((b, a, c)) #changing destination with source for intuitive convenience

    #part 1
    print(calculate(seeds, maps))

    #part 2
    '''
    didn't have time to optimize this part too much. Actually I've tried but failed, because I've tried to decrease input, 
    but after half an hour I've realized that my method doesn't affect it at all :D anyway I include it, maybe it would work
    for somebody else. I've decided to apply the same function for part 1 and both part 2 and run a brute force.'''

    '''
    TODO: rework it as follows:
    1. create a while = True loop and a counter.
    2. start calculating in the same manner as part 1 but in reverse - starting from locations. Increment counter for each iteration.
    3. once the counter equals one of the original seeds, break and return its value.'''

    import multiprocessing as mp
    
    ranges_for_ranges = []
    for i in range(0, len(seeds), 2):
        ranges_for_ranges.append([seeds[i], seeds[i] + seeds[i + 1]])
    print(ranges_for_ranges)
    
    temp_list = [[True, True] for i in range(0, len(ranges_for_ranges))]
    for i in range(0, len(ranges_for_ranges)):
        for j in range(0, len(ranges_for_ranges[i])):
            for k in range(0, len(ranges_for_ranges)):
                if ranges_for_ranges[i] == ranges_for_ranges[k]:
                    if ranges_for_ranges[i][0] >= ranges_for_ranges[i][1]:
                        ranges_for_ranges[i] = [0,0]
                    break
                if ranges_for_ranges[i][j] > ranges_for_ranges[k][0]\
                and ranges_for_ranges[i][j] < ranges_for_ranges[k][1]:
                    if temp_list[k][j] == True:
                        if j == 0:
                            ranges_for_ranges[i][j] = ranges_for_ranges[k][1]
                        else:
                            ranges_for_ranges[i][j] = ranges_for_ranges[k][0]
                        temp_list[i][0] = temp_list[i][1] = False

    pool = mp.Pool(processes=round(mp.cpu_count()/2))
    seeds_2 = []
    for i in range(0, len(ranges_for_ranges)):
        seeds_2.append([pool.apply_async(create_seeds_from_range, [ranges_for_ranges[i][0], ranges_for_ranges[i][1]]).get()])
        print(len(seeds_2))
    results = []
    for i in range(0, len(seeds_2)):
        results.append(pool.apply_async(calculate, [seeds_2[i], maps]).get())
        print(len(results))
    print(min(results))
import sys

sys.setrecursionlimit(9999999)

def navigate(x, y):
    possible_directions = []
    if x in "S|LJ" and y in "|F7":
        possible_directions.append("North")
    if x in "S-LF" and y in "-J7":
        possible_directions.append("Right")
    if x in "S|F7" and y in "|LJ":
        possible_directions.append("South")
    if x in "S-J7" and y in "-LF":
        possible_directions.append("Left")
    return possible_directions

def dfs(x, y):
    global counter
    counter += 1
    visited[y][x] = True
 
    if y - 1 > -1 and y - 1 < len(graph):
        if visited[y - 1][x] == False:
            if "North" in navigate(graph[y][x], graph[y - 1][x]):
                dfs(x,y-1)

    if x + 1 > -1 and x + 1 < len(graph[y]):
        if visited[y][x + 1] == False:
            if "Right" in navigate(graph[y][x], graph[y][x + 1]):
                dfs(x+1, y)

    if y + 1 > -1 and y + 1 < len(graph):
        if visited[y + 1][x] == False:
            if "South" in navigate(graph[y][x], graph[y + 1][x]):
                dfs(x,y + 1)

    if x - 1 > -1 and x - 1 < len(graph[y]):
        if visited[y][x - 1] == False:
            if "Left" in navigate(graph[y][x], graph[y][x - 1]):
                dfs(x - 1, y)

if __name__ == "__main__":
    with open("data/input_10.txt", "r") as file:
        items = file.read().rstrip().split('\n')

    graph   = [[x for x in row] for row in items]
    visited = [[False for _ in range(0, len(sublist))] for sublist in graph]
    start   = None

    for i, sublist in enumerate(graph):
        if "S" in sublist:
            start = [sublist.index("S"), i]
            sublist[sublist.index("S")] = 'F'

    counter = 0
    dfs(*start)
    print(counter//2)
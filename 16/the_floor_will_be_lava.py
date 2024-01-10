#todo part 2
def navigate(x, y, path, grid, visited, queue):
    if y < len(grid[0]) - 1 and (x, y + 1, 'Right') not in visited and (
            (path == 'Right' and grid[x][y] in '.-') or 
            (path == 'North' and grid[x][y] in '/-') or
            (path == 'South' and grid[x][y] in '\\-')):
        queue.add((x, y + 1, 'Right'))
        visited.add((x, y + 1, 'Right'))

    if x > 0 and (x - 1, y, 'North') not in visited and (
            (path == 'North' and grid[x][y] in '.|') or 
            (path == 'Right' and grid[x][y] in '/|') or
            (path == 'Left' and grid[x][y] in '\\|')):
        queue.add((x - 1, y, 'North'))
        visited.add((x - 1, y, 'North'))

    if y > 0 and (x, y - 1, 'Left') not in visited and (
            (path == 'Left' and grid[x][y] in '.-') or 
            (path == 'North' and grid[x][y] in '\\-') or
            (path == 'South' and grid[x][y] in '/-')):
        queue.add((x, y - 1, 'Left'))
        visited.add((x, y - 1, 'Left'))

    if x < len(grid) - 1 and (x + 1, y, 'South') not in visited and (
            (path == 'South' and grid[x][y] in '.|') or 
            (path == 'Right' and grid[x][y] in '\\|') or
            (path == 'Left' and grid[x][y] in '/|')):
        queue.add((x + 1, y, 'South'))
        visited.add((x + 1, y, 'South'))

if __name__=="__main__":

    with open("data/input_16.txt", "r") as file:
        items = file.read().rstrip().split('\n')

    grid = [list(r) for r in items]
    visited = set()
    energized = set()
    queue = set([(0, 0, 'Right')])   
    while queue:
        x, y, path = queue.pop()
        energized.add((x, y))
        navigate(x, y, path, grid, visited, queue)

    print(len(energized))
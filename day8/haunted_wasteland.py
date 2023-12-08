import re
from math import lcm
from functools import lru_cache, wraps
from frozendict import frozendict

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left}, {self.right})"
    
def freezeargs(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        args = tuple([frozendict(arg) if isinstance(arg, dict) else arg for arg in args])
        kwargs = {k: frozendict(v) if isinstance(v, dict) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapped

def traverse(graph, instructions, start, destination, count = 0):
    position = start
    for i in range(0, len(instructions)):
        position = graph[position].right if instructions[i] == "R" else graph[position].left
        if position == destination:
            return count + i + 1
    return traverse(graph, instructions, position, destination, count + len(instructions))

@freezeargs
@lru_cache(maxsize=None)
def traverse_2(graph, instructions, start, count = 0):
    position = start
    for i in range(0, len(instructions)):
        position = graph[position].right if instructions[i] == "R" else graph[position].left
        if position.endswith('Z'):
            return count + i + 1
    return traverse_2(graph, instructions, position, count + len(instructions))

if __name__ == "__main__":
    with open("data/input_8.txt", "r") as file:
        items = file.read().rstrip().split('\n')

    graph = {}
    instructions = items[0]

    for item in items[2:]:
        match = re.findall(r'\b[A-Z0-9]{3}\b', item)
        graph[match[0]] = Node(match[1], match[2])

    #part 1
    print(traverse(graph, instructions, 'AAA', 'ZZZ'))

    #part 2
    keys_part_2 = [key for key in graph.keys() if key.endswith('A')]
    print(keys_part_2)
    final_list = []
    for key in keys_part_2:
        final_list.append(traverse_2(graph, instructions, key))
    print(lcm(*final_list))
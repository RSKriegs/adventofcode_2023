import re

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left}, {self.right})"

def traverse(graph, instructions, start, destination, count = 0):
    position = start
    for i in range(0, len(instructions)):
        position = graph[position].right if instructions[i] == "R" else graph[position].left
        if position == destination:
            return count + i + 1
    return traverse(graph, instructions, position, destination, count + len(instructions))

if __name__ == "__main__":
    with open("data/input_8.txt", "r") as file:
        items = file.read().rstrip().split('\n')

    graph = {}
    instructions = items[0]

    for item in items[2:]:
        match = re.findall(r'\b[A-Z]{3}\b', item)
        graph[match[0]] = Node(match[1], match[2])

    print(traverse(graph, instructions, 'AAA', 'ZZZ'))
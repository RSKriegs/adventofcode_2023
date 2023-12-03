#day 1
with open("data/input_3.txt", "r") as file:
    items = file.read().rstrip().split('\n')

#create an initial matrix from input
matrix = []
for i in range(0, len(items)):
    matrix.append(list(items[i]))

#create an adjacency matrix
matrix_map = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] in "!@#$%^&*()_-+={}[]":
            for x in range(max(0, i - 1), min(i + 2, len(matrix))):
                    for y in range(max(0, j - 1), min(j + 2, len(matrix[0]))):
                        matrix_map[x][y] = True

# retrieve elements - create a string to be converted to the integer 
elements = []
to_convert_to_int = ''
to_append = False
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] in "0123456789":
            to_convert_to_int += str(int(matrix[i][j]))
            if matrix_map[i][j]:
                to_append = True
        else:
            if to_append:
                elements.append(int(to_convert_to_int))
            to_convert_to_int = ''
            to_append = False
        if j == len(matrix[0])-1 and to_append:
            elements.append(int(to_convert_to_int))

print(sum(elements))
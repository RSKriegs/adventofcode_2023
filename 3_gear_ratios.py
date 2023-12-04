#day 3
with open("", "r") as file:
    items = file.read().rstrip().split('\n')

#create an initial matrix from input
matrix = []
for i in range(0, len(items)):
    matrix.append(list(items[i]))
print(matrix)

#create an adjacency matrix
matrix_map = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] not in "0123456789.":
            for x in range(max(0, i - 1), min(i + 2, len(matrix))):
                    for y in range(max(0, j - 1), min(j + 2, len(matrix[0]))):
                        matrix_map[x][y] = True

# retrieve elements - create a string to be converted to the integer 
elements = []
for i in range(len(matrix)):
    to_convert_to_int = ''
    to_append = False
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

# print(sum(elements))

#2nd part
#create an adjacency matrix
matrix_map = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] in "*":
            symbol = matrix[i][j]
            count_adjacent = 0  # Counter for adjacent symbols
            for x in range(max(0, i - 1), min(i + 2, len(matrix))):
                for y in range(max(0, j - 1), min(j + 2, len(matrix[0]))):
                    if matrix[x][y] in '0123456789':
                        count_adjacent += 1
            if count_adjacent >= 2:  # If there are at least two adjacent symbols
                matrix_map[i][j] = True

# retrieve elements - create a string to be converted to the integer 
elements = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix_map[i][j]:
            to_convert_to_int = ''
            temp_list = []
            for x in range(max(0, i - 1), min(i + 2, len(matrix))):
                for y in range(max(0, j - 1), min(j + 2, len(matrix[0]))):
                    if matrix[x][y] in '0123456789':
                        to_convert_to_int = str(int(matrix[x][y]))
                        for z in range(y - 1, -1, -1):
                            if matrix[x][z] in '0123456789':
                                to_convert_to_int = str(int(matrix[x][z])) + to_convert_to_int
                                matrix[x][z] = '.'
                            else:
                                break
                        for z in range(y + 1, len(matrix[0])):
                            if matrix[x][z] in '0123456789':
                                to_convert_to_int += str(int(matrix[x][z]))
                                matrix[x][z] = '.'
                            else:
                                break
                        temp_list.append(to_convert_to_int)
                    else:
                        to_convert_to_int = ''
            if len(temp_list) > 1:
                print(temp_list)
                gear_ratio = 1
                for element in temp_list:
                    gear_ratio *= int(element)
                elements.append(gear_ratio)

print(sum(elements))
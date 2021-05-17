def col_product(matrix, row_index, col_index, length):
    i = 0
    product = 1
    while(i < length):
        product *= matrix[row_index+i][col_index]
        i += 1
    return product
def row_product(matrix, row_index, col_index, length):
    i = 0
    product = 1
    while(i < length):
        product *= matrix[row_index][col_index+i]
        i += 1
    return product
def diag_product(matrix, row_index, col_index, length):
    i = 0
    product = 1
    while(i < length):
        product *= matrix[row_index+i][col_index+i]
        i += 1
    return product
grid = []
with open("number_grid.txt") as f:
    for line in f:
        grid.append([int(i) for i in line.split()])
max_number = 1
row_number = 0
counter = 0
location = [0,0]
while(row_number < len(grid)):
    col_number = 0
    while(col_number < len(grid)):
        if(row_number+3 < len(grid) and col_number+3 < len(grid[0])):
            rp = row_product(grid, row_number, col_number, 4)
            cp = col_product(grid, row_number, col_number, 4)
            dp = diag_product(grid, row_number, col_number, 4)
            prev_max = max_number
            max_number = max(max_number, rp, cp, dp)
            if(prev_max != max_number):
                location = [col_number,row_number]
        elif(row_number+3 < len(grid)):
            prev_max = max_number
            max_number = max(max_number, col_product(grid, row_number, col_number, 4))
            if(prev_max != max_number):
                location = [col_number,row_number]
        elif(col_number+3 < len(grid[0])):
            prev_max = max_number
            max_number = max(max_number, row_product(grid, row_number, col_number, 4))
            if(prev_max != max_number):
                location = [col_number,row_number]
        col_number += 1
    row_number += 1
print(max_number)
print(location)

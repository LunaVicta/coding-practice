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
while(row_number < len(grid)):
    col_number = 0
    while(col_number < len(grid)):
        print(grid[row_number][col_number], end=" ")
        if(row_number+3 < len(grid) and col_number+3 < len(grid[0])):
            rp = row_product(grid, row_number, col_number, 4)
            cp = col_product(grid, row_number, col_number, 4)
            dp = diag_product(grid, row_number, col_number, 4)
            max_number = max(max_number, rp, cp, dp)
            counter += 3
        elif(row_number+3 < len(grid)):
            max_number = max(max_number, col_product(grid, row_number, col_number, 4))
            counter += 1
        elif(col_number+3 < len(grid[0])):
            max_number = max(max_number, row_product(grid, row_number, col_number, 4))
            counter += 1
        col_number += 1
    print()
    row_number += 1
print(max_number)
print(counter)

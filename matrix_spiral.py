 # matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
# matrix = [[32, 44, 27, 23], [54, 28, 50, 62]]
# matrix = [[1, 2, 3], [4, 5, 6]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
row_high = len(matrix) - 1
col_high = len(matrix[0]) - 1
row_low = 0
col_low = 0
row = 0
col = 0
res = []
while True:

    if col <= col_high:
        while col <= col_high:
            res.append(matrix[row][col])
            col += 1
        col -= 1
        row += 1
    else:
        break

    if row <= row_high:
        while row <= row_high:
            res.append(matrix[row][col])
            row += 1
        row -= 1
        col -= 1
    else:
        break

    if col >= col_low:
        while col >= col_low:
            res.append(matrix[row][col])
            col -= 1
        col += 1
        row -= 1
        row_low += 1
        col_low += 1
        row_high -= 1
        col_high -= 1
    else:
        break

    if row >= row_low:
        while row >= row_low:
            res.append(matrix[row][col])
            row -= 1
        row += 1
        col += 1
    else:
        break
print(res)
import copy
mat = [
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1]
]
temp = copy.deepcopy(mat)

for i in range(len(temp)):
    if 1 in temp[i]:
        j = 0
        while j < len(temp[i]):
            mat[i][j] = 1
            j += 1

r = 0

while r < len(temp):
    c = 0
    while c < len(temp[r]):
        if temp[r][c] == 1:
            i = 0
            while i < len(temp):
                mat[i][c] = 1
                i += 1
        c += 1
    r += 1

print(mat)
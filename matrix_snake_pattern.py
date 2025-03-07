matrix = [
    [45, 48, 54],
    [21, 89, 87],
    [70, 78, 15]
]

i = 0
j = 0
n = len(matrix)
arr = []

while i < n:
    if i % 2 == 0:
        j = 0
        while j < n:
            arr.append(matrix[i][j])
            j += 1
    else:
        j = n - 1
        while j >= 0:
            arr.append(matrix[i][j])
            j -= 1
    i += 1

print(arr)
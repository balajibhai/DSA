# arr = [1, 2, 3, 4, 5]
# arr = [2, 4, 7, 8, 9, 10]
arr = [1]
i = 0
l = len(arr)

while i < l:
    if i + 1 < l:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    i += 2

print(arr)
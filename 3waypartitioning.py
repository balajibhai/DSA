arr = [1, 4, 3, 6, 2, 1]
a = 1
b = 3
i = 0
j = i + 1
l = len(arr)

while (j < l):
    if (arr[i] < a):
        i += 1
    elif (arr[j] < a):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    j += 1

j = i + 1
while (j < l):
    if (arr[i] >= a) and (arr[i] <= b):
        i += 1
    elif (arr[j] >= a) and (arr[j] <= b):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    j += 1

print(arr)
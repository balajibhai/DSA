arr = [568, 498, 992, 688, 887]
l = len(arr)
min_from_left = arr[0]
max_from_right = arr[l - 1]
res = []
h = {}
i = 0
j = l - 2

while (i < l):
    if (arr[i] < min_from_left):
        min_from_left = arr[i]
    h[arr[i]] = [min_from_left]
    i += 1

while (j >= 0):
    if (arr[j] > max_from_right):
        max_from_right = arr[j]
    h[arr[j]].append(max_from_right)
    j -= 1

k = 1
while (k <= l - 2):
    current = arr[k]
    left_min = h[arr[k]][0]
    right_max = h[arr[k]][1]
    if (current > left_min) and (current < right_max):
        res = [left_min, current, right_max]
        break
    k += 1

if (len(res)):
    print(res)
else:
    print([])
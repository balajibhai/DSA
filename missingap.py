arr = [1, 6, 11, 16, 21, 31]
l = len(arr)
left = 0
right = l - 1
a1 = arr[0]
missing = 0
d = (arr[l-1] - arr[0])//(l)

while (left <= right):
    mid = (left + right) // 2
    n = mid + 1
    if (a1 + (n - 1) * d == arr[mid]):
        if (mid + 1 < l) and (arr[mid] + d != arr[mid + 1]):
            missing = arr[mid] + d
            break
        else:
            left = mid + 1
    else:
        if (mid - 1 >= 0) and (arr[mid] - d != arr[mid - 1]):
            missing = arr[mid] - d
            break
        else:
            right = mid - 1

print(missing)
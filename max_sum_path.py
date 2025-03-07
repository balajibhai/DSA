arr1 = [1, 2, 5, 8, 10]
arr2 = [1, 2, 3, 5, 9]
i = 0
j = 0
l1 = len(arr1)
l2 = len(arr2)
s1 = 0
s2 = 0
res = 0

while i < l1:
    if arr1[i] < arr2[j]:
        s1 += arr1[i]
        i += 1
    elif arr1[i] > arr2[j]:
        s2 += arr2[j]
        j += 1
    else:
        res += max(s1, s2) + arr1[i]
        s1 = s2 = 0
        i += 1
        j += 1
    if i == l1:
        break
    if j == l2:
        break

while i < l1:
    s1 += arr1[i]
    i += 1

while j < l2:
    s2 += arr2[j]
    j += 1

res += max(s1, s2)
print(res)
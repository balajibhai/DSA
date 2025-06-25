# https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

arr = [16, 17, 4, 3, 5, 2]
i = j = len(arr) - 1
res = []
while i >= 0:
    if arr[i] >= arr[j]:
        res.append(arr[i])
        j = i
    i -= 1

res.reverse()
print(res)
# https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1


arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
arr.sort()
l = len(arr)
min_so_far = 10**9
i = 0
j = i + m - 1
while True:
    min_so_far = min(arr[j] - arr[i], min_so_far)
    i += 1
    j += 1
    if j >= l:
        break

print(min_so_far)
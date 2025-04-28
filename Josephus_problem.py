# https://www.geeksforgeeks.org/problems/josephus-problem/1

n = 3
k = 2
# n = 5
# k = 3
arr = []

for i in range(n):
    arr.append(i + 1)

count = 1
i = 0

while len(arr) > 1:

    if count == k:
        arr.remove(arr[i])
        count = 0
    else:
        i += 1
    if i >= len(arr):
        i = 0

    count += 1

print(arr[0])
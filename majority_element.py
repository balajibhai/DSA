# https://www.geeksforgeeks.org/problems/majority-element-1587115620/1


arr = [2, 3]
# arr = [7]
# arr = [1, 1, 2, 1, 3, 5, 1]
h = {}
req = len(arr) // 2
flag = -1

for i in arr:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1

for i in h:
    if h[i] > req:
        flag = i
        break

print(flag)
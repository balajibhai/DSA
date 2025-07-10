# https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1

# arr = [2, 3, 1, 2, 3]
arr = [0, 3, 1, 2] 
h = {}
res = []

for i in arr:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1

for i in h:
    if h[i] > 1:
        res.append(i)

print(res)
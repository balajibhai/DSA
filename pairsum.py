arr = [1, 2, 3, 4, 5, 6, 7]
k=8
h = {}
t = 0
res = 0

for i in arr:
    h[i] = 1

for i in arr:
    t = k - i
    if t!=i and t in h and h[t]==1:
        h[t] = 2
        h[i] = 2
        res += 1

print(res)
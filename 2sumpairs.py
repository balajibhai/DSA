arr = [0,0,0]
h = {}
res = []
unique = []
for i in arr:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1
for i in h:
    unique.append(i)
unique.sort()
for i in unique:
    if i < 0:
        if abs(i) in h:
            res.append([i, abs(i)])
    if i == 0 and h[i] > 1:
        res.append([i, abs(i)])
print(res)
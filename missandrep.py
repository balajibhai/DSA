arr = [6, 5, 8, 7, 1, 4, 1, 3, 2]
h = {}
i = 0
l = len(arr)
res = []
temp = []

for i in range(1, l+1):
    temp.append(i)

i = 0
while (i < l):
    if arr[i] in h:
        h[arr[i]] += 1
        res.append(arr[i])
    else:
        h[arr[i]] = 1
    i += 1

for i in temp:
    if i not in h:
        res.append(i)
        break

print(res)
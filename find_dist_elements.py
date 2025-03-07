M = [[2, 1, 4, 3], [1, 2, 3, 2], [3, 6, 2, 3], [5, 2, 5, 3]]
N = 4
h = []
count = 0
for i in range(N):
    h.append({})

for i in range(N):
    for j in range(N):
        item = M[i][j]
        h[i][item] = 1

for find in h[0]:
    flag = 0
    for k in range(1, N):
        if find not in h[k]:
            flag = 0
            break
        else:
            flag = 1
    if flag:
        count += 1

print(count)
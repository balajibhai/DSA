a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 0, 1]
flag = 1
h1 = {}
h2 = {}
for i in a:
    if i in h1:
        h1[i] += 1
    else:
        h1[i] = 1
for i in b:
    if i in h2:
        h2[i] += 1
    else:
        h2[i] = 1
for i in a:
    if i in h2 and h2[i] != h1[i] or i not in h2:
        flag = 0
        break

if flag:
    print(True)
else:
    print(False)
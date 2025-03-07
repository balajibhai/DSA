s1 = "cbbdeccea"
s2 = "edbcddebb"
k = 5
h1 = {}
h2 = {}

if (len(s1) != len(s2)):
    print(False)

for i in s1:
    if i in h1:
        h1[i] += 1
    else:
        h1[i] = 1

for i in s2:
    if i in h2:
        h2[i] += 1
    else:
        h2[i] = 1

count = 0

for i in h1:
    if i in h2:
        if h1[i] != h2[i]:
            count += 1
    else:
        count += 1

if count <= k:
    print(True)
else:
    print(False)
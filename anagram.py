s1 = "a"
s2 = "b"
if (len(s1) != len(s2)):
    print(False)
h1 = {}
h2 = {}
flag = 0
for i in s1:
    if i in h1:
        h1[i] += 1
    else:
        h1[i] = 1

for j in s2:
    if j in h2:
        h2[j] += 1
    else:
        h2[j] = 1

for i in h1:
    if i not in h2 or h1[i] != h2[i]:
        print(False)
    else:
        flag = 1

if (flag):
    print(True)


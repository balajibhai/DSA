s1 = "geeksforgeeks"
s2 = "geeksquiz"
h1 = {}
h2 = {}
temp = ""
res = ""
for i in s1:
    h1[i] = 1
for i in s2:
    h2[i] = 1
for i in h1:
    if i not in h2:
        temp += i
for i in h2:
    if i not in h1:
        temp += i
temp = sorted(temp)
for i in temp:
    res += i
print(res)
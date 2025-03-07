str1 = "basgadhbfgvhads"
str2 = "sjdhgvbjdsbhvbvd"
h1 = {}
h2 = {}
count = 0

for i in str1:
    if i in h1:
        h1[i] += 1
    else:
        h1[i] = 1

for i in str2:
    if i in h2:
        h2[i] += 1
    else:
        h2[i] = 1

for i in h1:
    if i not in h2:
        count += h1[i]
    else:
        count += abs(h1[i] - h2[i])

for i in h2:
    if i not in h1:
        count += h2[i]

print(count)
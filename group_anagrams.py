# arr = ["act", "god", "cat", "dog", "tac"]
# arr = ["no", "on", "is"]
arr = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
h = {}
for i in arr:
    key = ''.join(sorted(i))
    if key in h:
        h[key].append(i)
    else:
        h[key] = []
        h[key].append(i)
res = []
for i in h:
    res.append(h[i])
print(res)
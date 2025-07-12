# https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1


# arr = [2, 6, 1, 9, 4, 5, 3]
# arr = [1, 9, 3, 10, 4, 20, 2]
arr = [15, 13, 12, 14, 11, 10, 9]
s = set(arr)
h = {}
maxsofar = -1
l = len(arr)

for i in arr:
    h[i] = 1
    
for i in s:
    if i - 1 not in h:
        count = 1
        while i + count in h:
            count += 1
        maxsofar = max(count, maxsofar)

print(maxsofar)
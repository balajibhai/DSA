# https://www.geeksforgeeks.org/problems/largest-fibonacci-subsequence2206/1
# arr = [1, 4, 3, 9, 10, 13, 7]
arr = [0, 2, 8, 5, 2, 1, 4, 13, 23]
max_num = max(arr)
fibonacci_hash = {}
f = 0
f1 = -1
f2 = 1
res = []

while f <= max_num:
    f = f1 + f2
    f1 = f2
    f2 = f
    fibonacci_hash[f] = 1

for i in arr:
    if i in fibonacci_hash:
        res.append(i)

print(res)
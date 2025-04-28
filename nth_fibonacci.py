# https://www.geeksforgeeks.org/problems/the-nth-fibonnaci3150/1

n = 3
f1 = 0
f2 = 1
f = 0
i = 0

while i < n-1:
    f = f1 + f2
    f1 = f2
    f2 = f
    i += 1

print(f % 10)

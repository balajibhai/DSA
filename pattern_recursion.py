# https://www.geeksforgeeks.org/problems/print-pattern3549/1
# n = 16
n = 10
# n = 0
arr = []
def pattern(n):
    arr.append(n)
    if n <= 0:
        return(n)
    return pattern(n - 5)

a = pattern(n)
print('a:', a)
t = arr[-1]

def pattern(t):
    arr.append(t)
    if t == n:
        return
    pattern(t + 5)

pattern(t+5)
print(arr)
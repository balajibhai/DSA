# https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1

# arr = [1, 2, 3, 4, 5]
# d = 2
# arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# d = 3
arr = [7, 3, 9, 1]
d = 9
n = len(arr)
d = d % n

def reverse_arr(i, j):
    while (i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

j = d - 1
i = 0
reverse_arr(i, j)
i = d
j = n - 1
reverse_arr(i, j)
arr.reverse()
print(arr)
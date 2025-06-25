# https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1

# arr = [2, 2, 2, 2, 2]
arr = [1, 2, 4]
i = 0 
n = len(arr)
count = 1
j = 1

while j < n:
    if arr[i] != arr[j]:
        count += 1
        i += 1
        arr[i] = arr[j]
    j += 1

print(count)
print(arr)
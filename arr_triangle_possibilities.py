# https://www.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1

# arr = [4, 6, 3, 7]
# arr = [10, 21, 22, 100, 101, 200, 300]
arr = [1, 2, 3]
arr.sort()
i = 0
n = len(arr)
count = 0

while i < n:
    j = i + 1
    while j < n:
        k = j + 1
        while k < n:
            if arr[i] + arr[j] > arr[k]:
                count += 1
            else:
                break
            k += 1
        j += 1
    i += 1

print(count)

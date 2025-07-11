# https://www.geeksforgeeks.org/problems/pair-with-given-sum-in-a-sorted-array4940/1


# arr = [-1, 1, 5, 5, 7]
# t = 6
# arr = [1, 1, 1, 1]
# t = 2
arr = [-1, 10, 10, 12, 15]
target = 125
l = len(arr) - 1
count = 0
left = 0
right = l

while left <= right:
    s = arr[left] + arr[right]
    if s < target:
        left += 1
    elif s > target:
        right -= 1
    else:
        if arr[left] == arr[right]:
            n = right - left + 1
            res = n * (n - 1) // 2
            count += res
            break
        
        lv = arr[left]
        lc = 0
        while left <= right and arr[left] == lv:
            lc += 1
            left += 1
        
        rv = arr[right]
        rc = 0
        while right >= left and arr[right] == rv:
            rc += 1
            right -= 1
        
        count += lc * rc

print(count)
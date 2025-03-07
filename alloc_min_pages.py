# https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
# arr = [12, 34, 67, 90]
# k = 2
# arr = [15, 10, 19, 10, 5, 18, 7]
# k = 5
arr = [13, 31, 37, 45, 46, 54, 55, 63, 73, 84, 85]
k = 9
# arr = [15, 17, 20]
# k = 5
# arr = [22, 23, 67]
# k = 1
l = len(arr)
low = max(arr)
high = sum(arr)
min_so_far = 1000000
if k > l:
    print(-1)
else:
    while low <= high:
        mid = (low + high)//2
        num = 1
        s = 0
        for i in arr:
            s += i
            if s > mid:
                num += 1
                s = i
            if num > k:
                break
        if num > k:
            low = mid + 1
        else:
            min_so_far = min(min_so_far, mid)
            high = mid - 1
    print(min_so_far)
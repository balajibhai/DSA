# https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
def pagealloc(arr, k):
    total = sum(arr)
    percentage = []
    min_percent = 100//k
    print("min_percent", min_percent)
    if(len(arr) < k):
        return -1
    for i in arr:
        percentage.append((i/total) * 100)
    print("percentage arr:", percentage)
    per_sum = [0] * len(percentage)
    j = len(percentage) - 1
    temp = 0
    while(j >= 0):
        per_sum[j] = temp
        temp += percentage[j]
        j -= 1
    print("percentage sum:", per_sum)
    s = 0
    val = 0
    maxi = 0
    # for i in range(len(percentage)):
    #     t = s + percentage[i]
    #     if t > min_percent:
    #         print('splitting', s)
    #         print(val)
    #         s = percentage[i]
    #         val = arr[i]
    #     else:
    #         s = t
    #         val += arr[i]
    for i in range(len(percentage)):
        if percentage[i] >= min_percent:
            s = percentage[i]
            val = arr[i]
        else:
            s += percentage[i]
            val += arr[i]
        if s >= min_percent:
            print('splitting', s)
            maxi = max(maxi, val)
            print(val)
            s = 0
            val = 0
    print(s)
    print(val)
    return(maxi)

arr = [12, 34, 67, 90]
k = 2
# arr = [15, 10, 19, 10, 5, 18, 7]
# k = 5
# arr = [22, 23, 67]
# k = 1
# arr = [13, 31, 37, 45, 46, 54, 55, 63, 73, 84, 85]
# k = 9
# arr = [85, 85, 10]
# k = 2
print(pagealloc(arr, k))
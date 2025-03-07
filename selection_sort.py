arr = [4, 1, 3, 9, 7]
i = 0
l = len(arr)
index = 0
while(i < l):
    min_so_far = 10**7
    j = i
    while(j < l):
        if(arr[j] <= min_so_far):
            min_so_far = arr[j]
            index = j
        j += 1
    arr[i], arr[index] = arr[index], arr[i]
    i += 1
print(arr)
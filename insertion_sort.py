arr = [1593, 3254, 481, 1706, 1102, 4089, 1301, 6297, 5558, 7463, 4089]
k = 1
l = len(arr)
while(k < l):
    j = 0
    while(j<k):
        if(arr[k] <= arr[j]):
            t = arr[k]
            arr.pop(k)
            arr.insert(j, t)
            break
        j += 1
    k += 1
print(arr)
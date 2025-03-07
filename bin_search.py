arr = [2, 3, 7, 10, 12]
a = 2
left = 0
right = len(arr) - 1

while(left<=right):
    mid = (left+right)//2
    if(arr[mid] == a):
        print('element found at index:', mid)
        break
    elif(arr[mid] > a):
        right = mid - 1
    else:
        left = mid + 1


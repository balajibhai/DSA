arr = [6, 9, 9]
l = len(arr)
left_max = [0]
right_max = [0] * l
max_so_far = 0
res = 0

for i in range(1, l):
    if arr[i-1] >= max_so_far:
        max_so_far = arr[i-1]
    left_max.append(max_so_far)

j = l - 2
max_so_far = -1

while (j >= 0):
    if arr[j+1] >= max_so_far:
        max_so_far = arr[j+1]
    right_max[j] = max_so_far
    j -= 1

i = 0
smaller = 0
while(i<l):
    smaller = min(left_max[i], right_max[i])
    if(smaller-arr[i] >= 0):
        res += smaller-arr[i]
    else:
        res += 0
    i+=1

print(left_max)
print(right_max)
print(res)
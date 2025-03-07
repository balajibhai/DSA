arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
left_min = []
right_max = []
min_so_far = 100000000
max_so_far = -1
curr_index = 0
max_diff = 0
l = len(arr)

for i in arr:
    if (i < min_so_far):
        min_so_far = i
    left_min.append(min_so_far)

j=l-1
while(j>=0):
    if (arr[j] > max_so_far):
        max_so_far = arr[j]
    right_max.append(max_so_far)
    j-=1
right_max.reverse()
i = 0
j = 0

while (j < len(right_max)):
    if (left_min[i] < right_max[j]):
        curr_index = j - i
        if (curr_index > max_diff):
            max_diff = curr_index
        j += 1
    else:
        i += 1
    if (i > j):
        j = i

print(max_diff)
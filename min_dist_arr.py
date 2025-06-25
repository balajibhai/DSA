# https://www.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1

# arr = [1,2,3,2]
# x = 1
# y = 2

# arr = [86, 39, 90, 67, 84, 66, 62]
# x = 42
# y = 12

arr = [10, 20, 30, 40, 50]
x = 10
y = 50

x_index = y_index = -1
min_so_far = 10**5
for i in range(len(arr)):
    if x == arr[i]:
        x_index = i
    if y == arr[i]:
        y_index = i
    if x_index > -1 and y_index > -1:
        min_so_far = min(min_so_far, abs(x_index - y_index))

if x_index > -1 and y_index > -1:
    print(min_so_far)
else:
    print(-1)
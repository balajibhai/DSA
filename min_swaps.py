# https://www.geeksforgeeks.org/problems/minimum-swaps/1
arr = [32524, 30965, 30657, 18612, 29956, 15628, 16059, 10826, 23546, 22340]
temp = arr.copy()
l = len(temp)
arr.sort()
count = 0
for i in range(l):
    if temp[i] != arr[i]:
        count += 1
print(count//2)

# [2,3,1]
# [1,2,3]
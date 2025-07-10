# https://www.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1

# arr = [100, 180, 260, 310, 40, 535, 695]
# arr = [4, 2, 2, 2, 4]
arr = [4, 2]
i = 0
l = len(arr)
cumu = 0

while i < l:
    if i + 1 < l and arr[i + 1] > arr[i]:
        cumu += arr[i + 1] - arr[i]
    i += 1

print(cumu)
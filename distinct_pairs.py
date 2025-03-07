# https://www.geeksforgeeks.org/problems/count-distinct-pairs-with-difference-k1233/1
# nums = [11, 6, 10, 5, 11, 16]
# k = 5
nums = [1,5,3]
k = 2
count_hash = {}
pairs = 0
unique = []
for i in nums:
    if i in count_hash:
        count_hash[i] += 1
    else:
        count_hash[i] = 1

for i in count_hash:
    unique.append(i)

if (k == 0):
    for i in unique:
        if i in count_hash:
            if count_hash[i] > 1:
                pairs = 1
                break
    if pairs:
        print(pairs)

for i in unique:
    if i + k in count_hash:
        pairs += 1

print(pairs)

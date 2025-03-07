# https://www.geeksforgeeks.org/problems/winner-of-an-election-where-votes-are-represented-as-candidate-names-1587115621/1
arr = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]
res = []
h = {}
max_so_far = -1
curr_max_str = ""
final_contestants = []

for i in arr:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1
    if h[i] > max_so_far:
        max_so_far = h[i]
        curr_max_str = i

for i in h:
    if h[i] == max_so_far:
        final_contestants.append(i)

final_contestants.sort()

print(h)
print(curr_max_str)
print(final_contestants[0])
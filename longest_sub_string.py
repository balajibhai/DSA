s = "dvdf"
temp = ""
max_so_far = ""

for i in s:
    if (len(temp) > len(max_so_far)):
        max_so_far = temp
    if i not in temp:
        temp += i
    else:
        temp = i

print(len(max_so_far))
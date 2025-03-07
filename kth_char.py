m = 5
n = 2
k = 5
binary = str(bin(m)[2:])
temp_str = binary
for i in range(n):
    temp_list = list(temp_str)
    j = 0
    l = len(temp_list)
    while (j < l):
        if (temp_list[j] == "0"):
            temp_list[j] = "01"
        else:
            temp_list[j] = "10"
        j += 1
    temp_str = "".join(temp_list)

print(temp_str[k - 1])
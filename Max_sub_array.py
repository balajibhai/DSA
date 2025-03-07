n = 5
a = [1, 2, -1, 3, 4]
total = 0
max_total = 0
i = 0
starting_index = i
ending_index = n - 1
after_neg = i
res = []
max_arr_len = 0
arr_len = 0
while (i < n):
    if (a[i] >= 0):
        total += a[i]
        if(total >= max_total):
            max_total = total
            arr_len = i-after_neg+1
            if(max_arr_len <= arr_len):
                max_arr_len = arr_len
                if(after_neg <= starting_index):
                    starting_index = after_neg
                    ending_index = i
    else:
        after_neg = i + 1
        # ending_index = i - 1
        total = 0
    i += 1

for j in range(starting_index, ending_index + 1):
    res.append(a[j])
print(res)
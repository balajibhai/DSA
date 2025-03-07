# 3
# 333222111
# 332211
# 321

# loop to get the no of rows(n)
# current_index=0 => to_print(n-currentIndex)
# loop over n till 1
    # print the current_no till to_print

# 3 rows to printed
# CI = 0 => to_print = 3
# 3-2-1
    # 3*32*31*3

# CI =1 -> to_print = 2
# 3-2-1
 # 3*22*21*2

# CI = 2

n = 0
for current_index in range(n):
    to_print = n - current_index
    for current_number in reversed(range(1, n+1)):
        for print_index in range(to_print):
            print(current_number, end="")
    print()


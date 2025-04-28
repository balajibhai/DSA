# https://www.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates0744/1

# s = "abccbccba"
# s = "aaaaa"
# s = "add"
s = "abc"
s = "geeksforgeek"
str_arr = list(s)
while True:
    i = 0
    j = 1
    is_char_equal = 0
    never_equal = 0

    while j < len(str_arr):
        if str_arr[i] != str_arr[j]:
            if is_char_equal:
                del str_arr[i:j]
                j = i
            else:
                i = j
            is_char_equal = 0
        else:
            is_char_equal = 1
            never_equal = 1
        j += 1

        if is_char_equal and j == len(str_arr):
            del str_arr[i:j]

    if never_equal == 0 or len(str_arr) == 0:
        break

print(''.join(str_arr))
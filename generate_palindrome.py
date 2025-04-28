def find_palindrome(str_len, s1, l, r, res):
    flag = 0
    while l >= 0 and r < str_len and s1[l] == s1[r]:
        flag = 1
        l -= 1
        r += 1
    else:
        if flag:
            temp = s1[l + 1: r]
            res.append(temp)

s1 = "racecarannakayak"
# s1 = "abc"
res = []
i = 0
str_len = len(s1)

while i < str_len:
    l = i - 1
    r = i + 1
    find_palindrome(str_len, s1, l, r, res)
    if r < str_len and s1[i] == s1[r]:
        find_palindrome(str_len, s1, l + 1, r, res)
    i += 1

print(res)
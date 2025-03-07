s1 = "11"
s2 = "0"
l1 = len(s1)
l2 = len(s2)
temp_arr = [0]*(l1 + l2)
num_rev1 = s1[::-1]
num_rev2 = s2[::-1]
i = 0
carry = 0
while(i < l2):
    j = 0
    while(j < l1):
        if(num_rev2[i] != '-') and (num_rev1[j] != '-'):
            res = int(num_rev2[i]) * int(num_rev1[j])
            carry = res//10
            rem = res % 10
            temp_arr[i+j] += rem
            temp_arr[i+j+1] += carry
        j += 1
    i += 1

temp_arr.reverse()
while(True):
    if (len(temp_arr) == 0):
        temp_arr = [0]
        break
    if(temp_arr[0] != 0):
        break
    if(temp_arr[0] == 0):
        temp_arr.remove(temp_arr[0])
res = ""
for i in temp_arr:
    res += str(i)

if(s1[0] == '-') and (s2[0] == '-'):
    print(res)
elif(s1[0] == '-') or (s2[0] == '-'):
    print('-' + res)
else:
    print(res)
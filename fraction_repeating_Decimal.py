# https://www.geeksforgeeks.org/problems/a-simple-fraction0921/1
from decimal import Decimal, getcontext
getcontext().prec = 50
a = 50
b = 22
# a = 22
# b = 7
# a = 1
# b = 2
# a = 11
# b = 18
h = {}
q = a // b
r = a % b
count = 0
res_str = ""
req_index = 0

if r == 0:
    print(q)

while True:
    q = (r * 10) // b
    r = (r * 10) % b
    print('q', q)
    print('r', r)
    if r == 0:
        break
    if r in h:
        req_index = h[r]
        break
    else:
        h[r] = req_index
    count += 1
    req_index += 1

temp = list(str(Decimal(a) / Decimal(b)))
i = 0
l = len(temp)
while i < l:
    if i > 0 and temp[i - 1] == ".":
        temp.insert(i, '(')
        temp.insert(i+count+1, ')')
        break
    i += 1
if r == 0:
    print(a / b)

joined_str = ''.join(temp)
index = joined_str.find(')') + 1
res_str = joined_str[:index]

print("count", count)
print("res_str", res_str)
print("req_index", req_index)

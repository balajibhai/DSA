s = " i like this program very much "
temp = s.split(" ")
l = len(temp)
i = l-1
res = ""
while(i>=0):
    if (temp[i] != ""):
        res += temp[i]+" "
    i-=1
i = len(res)-1
res = res[:i] + "" + res[i+1:]
print(res)
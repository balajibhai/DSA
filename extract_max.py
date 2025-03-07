S="100klh564abc365bg"
maxsofar = -2
temp = ""
for i in S:
    try:
        t = int(i)
        temp += t + int(i)
    except ValueError:
        temp = i
    if (temp != "" and int(temp) > maxsofar):
        maxsofar = temp

print(maxsofar)
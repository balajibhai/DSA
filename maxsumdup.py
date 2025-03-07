arr = [1, 0]
total = 1
pro = []
count = 0
pro_except_zero = 1
for i in arr:
    if(i == 0):
        count+=1
    else:
        pro_except_zero*=i
    total*=i
for i in arr:
    # if(i!=0):
    #     pro.append(total//i)
    # else:
    #     if(count>1):
    #         pro.append(0)
    #     else:
    #         pro.append(total)
    if(i == 0) and (count == 1):
        pro.append(pro_except_zero)
    elif(i == 0) and (count > 1):
        pro.append(0)
    else:
        pro.append(total//i)
print(pro)
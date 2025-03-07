# txt = "nxtipemjbxualljkxgbbwmkxouqeyegvkildhxcqsfayer"
# pat = "bwmkxouqeyegvkildhxcqsfayer"
# txt = "weqnfscp"
# pat = "eqnfscp"
# txt = "dicw"
# pat = "w"
txt = "larbjrpjjjgh"
pat = "jjgh"
i = 0
j = 0
l1 = len(txt)
l2 = len(pat)
index = -1
while j < l1:
    if ((l2 == 1) and (pat[i] == txt[j])) or (i >= l2-1) and (l2 != 1):
        index = j - l2 + 1
        break
    # if(i >= l2-1):
    #     index = j - l2
    #     break
    if i+1 < l2 and j+1 < l1 and pat[i] == txt[j] and pat[i+1] == txt[j+1]:
        i += 1
    else:
        i = 0
        j-=1
        index  = -1
    j += 1

print(index)
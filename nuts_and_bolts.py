order = ["!", "#", "$", "%", "&", "*", "?", "@", "^"]
nuts = ["@","%","$","#","^"]
bolts = ["%","@","#","$","^"]
nut = {}
bolt = {}
nut_len = len(nuts)
bolt_len = len(bolts)

for i in nuts:
    nut[i] = 1

for i in bolts:
    bolt[i] = 1
j = 0
for i in range(9):
    if order[i] in nut and j < nut_len:
        nuts[j] = order[i]
        j += 1
bolts = nuts
print(nuts)
print(bolts)
s1 = "timetopractice"
s2 = "toc"
# s1 = "zoom"
# s2 = "zooe"
# s1 = "zoomlazapzo"
# s2 = "oza"
need = {}
have = {}
formed = 0
required = len(s2)
left = 0
right = 0
l = len(s1)
res_arr = []
for i in s2:
    if i in need:
        need[i] += 1
    else:
        need[i] = 1
while(right < l):
    item = s1[right]
    if item in have:
        have[item] += 1
    else:
        have[item] = 1
    if item in need and have[item] == need[item]:
        formed += 1
    if formed == required:
        while(left <= right):
            element = s1[left]
            have[element] -= 1
            if element in need and have[element] < need[element]:
                res_arr.append({"start": left, "end": right})
                left = right + 1
                formed = 0
                have = {}
                break
            left += 1
    right += 1

if(len(res_arr) > 0):
    min_so_far = res_arr[0]["end"] - res_arr[0]["start"]

i = 0
index = 0
while i < len(res_arr):
    temp = res_arr[i]["end"] - res_arr[i]["start"]
    if(temp < min_so_far):
        min_so_far = temp
        index = i
    i += 1

start_index = res_arr[index]["start"]
end_index = res_arr[index]["end"]
res = ""
for i in range(start_index, end_index+1):
    res += s1[i]

print(need)
print(have)
print(res_arr)
if len(res_arr) > 0:
    print(res)
else:
    print("")
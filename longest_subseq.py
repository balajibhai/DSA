arr = [
    53, 57, 77, 15, 78, 58, 17, 63, 90, 73, 68, 82, 40, 68, 22, 52,
    81, 92, 80, 37, 62, 17, 76, 67, 55, 56, 20, 22, 37, 71, 65, 7,
    30, 93, 1, 1, 90, 46, 36, 74, 0, 37, 76, 69, 39, 97, 39, 30, 14,
    89, 74, 71, 27, 79, 51, 45, 51, 54, 90, 35, 68, 38, 7, 82, 55,
    65, 14, 40, 20, 64, 89, 95, 8, 43, 14, 88, 5, 24, 72, 9, 56, 17,
    60, 91, 16, 94, 47, 15, 33
]
arr.sort()
max_length = -1
i = 0
l = len(arr)
count = 1

while (i < l):
    if (i + 1 < len(arr)):
        if(arr[i] + 1 == arr[i + 1]):
            count += 1
        if (count > max_length):
            max_length = count
        if (arr[i] + 1 < arr[i + 1]):
            count = 1
    i += 1

print(max_length)
arr = ["Hi", "How", "are", "you", "Hi"]
word1 = "Hi"
word2 = "you"
word1_list = []
word2_list = []
index = 0
distance = 0

for i in arr:
    if word1 == i:
        word1_list.append(index)
    if word2 == i:
        word2_list.append(index)
    index+=1

word_index = 0

# word1_list = [8, 11, 13, 32, 45]
# word2_list = [1, 24, 25, 33, 34, 56]
word1_list = [8, 11, 13, 19, 32, 45]
word2_list = [1, 24, 25, 33, 34, 56]
min_so_far = abs(word2_list[0] - word1_list[0])
#Binary search
first_to_iterate = []
second_to_iterate = []
if(len(word1_list) < len(word2_list)):
    first_to_iterate = word1_list
    second_to_iterate = word2_list
else:
    first_to_iterate = word2_list
    second_to_iterate = word1_list
print(first_to_iterate)
print(second_to_iterate)
length_of_second_to_iterate = len(second_to_iterate)
# iterate arr
# motto is to find the element equal the current element
# find the mid_element of the other array
# If the mid_element is smaller than the current element, traverse towards right, else towards left
# repeat the process until the left and right pointers meet at the same index
# Finally, if the mid_element is greater than the current element, then subtract the immediate left of mid_element at last from the current element and find min_so_far
# else subtract the immediate right and find min_so_far
# If the subtracting index is negative or larger that the length of the other array, then subtract the current index and find min_so_far


for current in first_to_iterate:
    print('current', current)
    left = 0
    right = len(second_to_iterate) - 1
    mid_index = (left + right) // 2
    while(left!=right):
        print('left', left)
        print('right', right)
        mid_index = (left + right) // 2
        print('mid_index', mid_index)
        mid_element = second_to_iterate[mid_index]
        print('mid_element', mid_element)
        if(mid_element < current):
            if(mid_index + 1 == right):
                left = right - 1
            else:
                left = mid_index + 1
        else:
            if(mid_index - 1 < left):
                right = left
            else:
                right = mid_index - 1
    mid_index = (left + right) // 2
    mid_element = second_to_iterate[mid_index]
    print('mid_index outside loop', mid_index)
    print('mid_element outside loop', mid_element)
    if(mid_element > current):
        if(mid_index - 1 >= left):
            distance = abs(current - second_to_iterate[mid_index - 1])
        else:
            distance = abs(current - mid_element)
    if (mid_element < current):
        if(mid_index+1 < right):
            distance = abs(current - second_to_iterate[mid_index + 1])
        else:
            distance = abs(current - mid_element)
    print('distance', distance)
    if(distance < min_so_far):
        min_so_far = distance

print(min_so_far)

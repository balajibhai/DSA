arr = ["abc", "abcd", "ab"]
# arr.reverse()
char_index = 0
word_index = 1
temp = ""
first_word = arr[0]
flag = 1
while(char_index < len(first_word)):
    while(word_index < len(arr)):
        if(len(arr[word_index]) <= char_index) or (first_word[char_index] != arr[word_index][char_index]):
            flag = 0
            break
        word_index+=1
    word_index = 1
    if(flag):
        temp+=first_word[char_index]
    else:
        break
    char_index+=1

print(temp)
# while(i<len(arr)):
#     while(j<len(arr[i])):

# "ab"
# "a"
# "a" arr[1][i] ("a")
#   if(equal):
#       increment i
#   else:
#       break


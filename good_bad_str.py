# https://www.geeksforgeeks.org/problems/good-or-bad-string1417/1


def isGoodorBad(self, S):
    # code here 
    vowel = 1
    consonant = 1
    i = 0
    l = len(S)
    arr = ['a', 'e', 'i', 'o', 'u']
    flag = 1
    
    while i < l:
        if i + 1 < l:
            if S[i] in arr and S[i+1] in arr or S[i] in arr and S[i+1] == '?':
                vowel += 1
            else:
                vowel = 1
            if S[i] not in arr and S[i+1] not in arr or S[i] not in arr and S[i+1] == '?':
                consonant += 1
            else:
                consonant = 1
            if vowel > 5 or consonant > 3:
                flag = 0
                break
            else:
                flag = 1
        i += 1
    
    if flag:
        return 1
    else:
        return 0
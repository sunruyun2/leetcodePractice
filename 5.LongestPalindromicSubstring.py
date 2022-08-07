# 1.brute force, time limit exceed
def longestPalindrome(s:str)->str:
    res = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                res = max (res, j - i)

    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s[i:j] == s[i:j][::-1] and j - i == res:
                return s[i:j]

#2. Solution - the longest common substring
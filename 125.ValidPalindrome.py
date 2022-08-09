# intuition - edit the string and determine if it is palindrome
# lower() and isalpha() and isnumeric
# problem - maybe not allowed to use built-in function - may not allow to use extra memory
def isPalindrome(s:str)->bool:
    s = s.lower()
    res = ""
    for char in s:
        if char.isnumeric() or char.isalpha():
            res += char
    return res == res[::-1]

# print(isPalindrome("A man, a plan, a canal: Panama"))
# print(isPalindrome("race a car"))
# print(isPalindrome(" "))


# 2.two pointer and ascii number
def isPalindrome(s:str):
    l , r = 0 , len(s) - 1

    def isAlphanumeric(c):
        return (ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z") 
            or ord("0") <= ord(c) <= ord("9"))

    while l < r:
        while l < r and not isAlphanumeric(s[l]):
            l +=1
        while l < r and not isAlphanumeric(s[r]):
            r -=1

        if s[r].lower() != s[l].lower():
            return False

        l , r = l+ 1, r -1
    return True



print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
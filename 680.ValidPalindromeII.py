def validPalindrome(s:str):
    def skipLeft():
        l, r = 0, len(s) -1
        skip = 1
        while l<r:
            if s[l] == s[r]:
                l +=1
                r -=1
            elif skip == 1:
                skip -=1
                l +=1
            else:
                return False
        return True
    def skipRight():
        l, r = 0, len(s) -1
        skip = 1
        while l<r:
            if s[l] == s[r]:
                l +=1
                r -=1
            elif skip == 1:
                skip -=1
                r -=1
            else:
                return False
        return True
    return skipLeft() or skipRight()
    
s = "aba"
s = "abca"
s = "abc"
s = "abbbca"
print(validPalindrome(s))
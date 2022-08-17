# 1.brute force - nested loops
def strStr(haystack:str, needle:str)->int:
    for i in range(len(haystack)):
        if haystack[i] == needle[0] and i + len(needle) <= len(haystack):
            start = i
            for i2 in range(len(needle)):
                if haystack[i + i2] != needle[i2]:
                    start = -1
                    break
            if start!= -1:
                return start
    return -1

print(strStr("hello", "ll"))
print(strStr("aaaaa", "bba"))
print(strStr("hello", "ooo"))
print(strStr("a", "a"))


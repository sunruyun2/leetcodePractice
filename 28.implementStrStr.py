# 1.brute force - nested loops, time complexity O(n*m), nested for loop
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

# rewrite the code
def strStr(haystack, needle):
    if needle == "":
        return 0

    for i in range(len(haystack) + 1 - len(needle)):
        # for j in range(len(needle)):
        #     if haystack[i + j] == haystack[j]:
        #         break
        #     if j == len(needle):
        #         return i
        if haystack[i:i + len(needle)] == needle:
            return i
        return -1


# 2. KMP - a string match algorithm, can make time complexity O(n + m), but space complextiy O (n)
# try 
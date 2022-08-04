# 1.brute force, two pointer
def lengthOfLongestSubString(s:str)->int:
    maxLength = [0]
    for i in range(len(s)):
        length = 0
        seen = []
        for j in range(i,len(s)):
            if s[j] not in seen:
                seen.append(s[j])
                length +=1
            else:
                break
        maxLength.append(length)

    return max(maxLength)

print(lengthOfLongestSubString("abcabcbb"))
print(lengthOfLongestSubString("bbbbb"))
print(lengthOfLongestSubString("pwwkew"))
print(lengthOfLongestSubString(""))

# 2. sliding windows, I didn't solve it, I copy it
def lengthOfLongestSubString(s:str):
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l +=1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res
# I've solved a similar one
def wordPattern(pattern:str, s:str):
    s = s.split(" ")
    match1 = {}
    match2 = {}
    if len(pattern)!= len(s):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in match1.keys():
            match1[pattern[i]] = s[i]
        else:
            if s[i] != match1[pattern[i]]:
                return False
        if s[i] not in match2.keys():
            match2[s[i]] = pattern[i]
        else:
            if pattern[i] != match2[s[i]]:
                return False
    return True
pattern = "abba"
s = "dog cat cat dog"

pattern = "abba"
s = "dog cat cat fish"

pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
        


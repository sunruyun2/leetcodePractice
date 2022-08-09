def isIsmorphic(s:str, t:str):
    map1 = {}
    map2 = {}
    for i in range(len(s)):
        if s[i] not in map1.keys():
            map1[s[i]] = t[i]
        if t[i] not in map2.keys():
            map2[t[i]] =  s[i]
        if t[i] != map1[s[i]] or s[i] != map2[t[i]]:
                return False
    return True

print(isIsmorphic("egg", "add"))
print(isIsmorphic("paper", "title"))
print(isIsmorphic("foo", "bar"))
print(isIsmorphic("badc", "baba"))

# count or hashmap
# or array

# non-test version

def valid_anagram(s:str, t:str):

    for letter in s:
        if s.count(letter) != t.count(letter):
            return False
    return True

# s = 'anagram'
# t = 'nagaram'
# print(valid_anagram(s,t))
# s = 'rat'
# t = 'cat'
# print(valid_anagram(s,t))

# non-test version
def use_array(s,t):
    s = list(s)
    t = list(t)
    for letter in s:
        if letter not in t:
            return False
        t.remove(letter)
    return len(t) == 0

# s = 'anagram'
# t = 'nagaram'
# print(use_array(s,t))
# s = 'rat'
# t = 'cat'
# print(use_array(s,t))

class Solution:
    def hash_map(self,s,t):
        # return Counter(s) == Counter(c)

        if len(s) != len(t)
        count_s, count_t = {},{}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i],0)
            count_s[s[i]] = 1 + count_s.get(s[i],0)
        for c in count_s:
            if count_s[c] != count_t.get(c,0):
                return False
        return True


# we could also use sort


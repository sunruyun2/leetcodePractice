# 1.brute force, set
# time limit Exceeded
def findRepeatedDnaSequences(s:str)->list:
    repeatedList = set()
    returnList = []
    for i in range(len(s) - 10 + 1):
        for j in range(i+1, len(s) - 10 + 1):
            if s[i:i+10] == s[j :j+10]:
                repeatedList.add(s[i:i+10])
    
    return returnList

# print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

def findRepeatedDnaSequeneces2(s:str)->list:
    seen , output = set() , set()
    for i in range(len(s) -10 +1):
        if s[i:i+10] in seen:
            output.add(s[i:i+10])
        else:
            seen.add(s[i:i+10])

    return output

print(findRepeatedDnaSequeneces2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))


# 1.set 2.hash 3.

# hash table
def repeatedDnaSequences(s:str)->list:
    seen = {}
    output = []
    for i in range(len(s)-10 +1 ):
        seen.setdefault(s[i:i+10],0)
        seen[s[i:i+10]] +=1

    for key,value in seen.items():
        if value >=2:
            output.append(key)

    return output

print(repeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
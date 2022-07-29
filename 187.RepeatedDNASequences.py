# 1.brute force, set
def findRepeatedDnaSequences(s:str)->list:
    repeatedList = set()
    returnList = []
    for i in range(len(s) - 10 + 1):
        for j in range(i+1, len(s) - 10 + 1):
            if s[i:i+10] == s[j :j+10]:
                repeatedList.add(s[i:i+10])

    for sequence in repeatedList:
        returnList.append(sequence)
    
    return returnList

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
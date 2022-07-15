
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    dict = {}
    return_list = []
    for word in strs:
        dict[word] = sorted(word)

    for i,word1 in enumerate(strs):
        for j, word2 in enumerate(strs):
            if dict[word1] == dict[word2] and i!=j:
                if i > j:
                    return_list


    return dict

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))



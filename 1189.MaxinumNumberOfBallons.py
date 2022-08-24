# intuition - hash map
def maxNumberOfBalloons(text:str)->int:
    count = {"b": 0 ,"a": 0, "l":0, "o":0, "n": 0}
    for char in text:
        if char in count.keys():
            count[char] +=1

    count["l"] = count["l"] // 2
    count["o"] = count["o"] // 2
    return min(count[val] for val in count.keys())


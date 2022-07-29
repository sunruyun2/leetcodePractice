# 1.tuition
def lengthOfLastWord(s:str):
    s = s.strip()
    i = 0
    for letter in s:
        if letter == " ":
            i = 0
        else:
            i +=1

    return i

print(lengthOfLastWord("hello world"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))
print(lengthOfLastWord("l"))
print(lengthOfLastWord(""))
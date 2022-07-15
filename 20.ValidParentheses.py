def isValid(s:str):
    stack = []
    openToClose = {")":"(" , "]":"[","}":"{"}

    for letter in s:
        if letter in openToClose.keys():
            # if the stack is empty or the parentheses are not matching up
            if len(stack) == 0:
                return False
            if stack[-1] == openToClose[letter]:
                stack.pop()
            else:
                return False
        else:
            stack.append(letter)
    return len(stack) == 0

print(isValid("()"))
print(isValid('()[]{}'))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("(){}}{"))

def betterversion(s:str):
    stack = []
    openToClose = {")":"(" , "]":"[","}":"{"}

    for c in s:
        if c in openToClose.keys():
            if stack[-1] == openToClose[c] and stack:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False
    

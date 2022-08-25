# 1.intuition - apparently it is binary search
def guessNumber(n:int):
    l , r = 1 , n
    while l < r:
        mid = l + (r - l) // 2
        if guess(mid) == -1:
            r = mid
        elif guess(mid) == 1:
            l = mid + 1
        else:
            return mid
    return l

print(guessNumber(10))
from re import I


# 1.intuition - brute force
def arrangeCoins(n:int)->int:
    i = 0
    while n>=0:
        i +=1
        n = n - i
        if n == 0:
            return i
    return i - 1
print(arrangeCoins(5))

# 2.improve - binary search
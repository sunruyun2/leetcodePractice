# intuition
def hamingWeight(n:int)->int:
    res = 0
    while n:
        res += n % 2
        n = n //2
        # n = n >> 1 also works:shift 1 bit to the right
    return res


# another solution
def hamingWeight(n:int)->:
    res = 0
    while n:
        n = n & (n-1)
        res+=1
    return res
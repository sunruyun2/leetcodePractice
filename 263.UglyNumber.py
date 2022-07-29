# 1. tuition
# negative number, catch the end case
def isUgly(n:int)->bool:
    if n <=0:
        return False
    primeFactor = 2
    while n !=1:
        if primeFactor >5:
            return False
        if n % primeFactor == 0:
            n = n // primeFactor
        else:
            primeFactor +=1
    return True

# print(isUgly(1))
# print(isUgly(10))
# print(isUgly(6))
# print(isUgly(121))
# print(isUgly(20))
# print(isUgly(-2147483648))
# print(isUgly(905391974))

# solution answer, silly me
def isUgly(n:int)->bool:
    if n <= 0:
        return False
    for i in [2,3,5]:
        while n % i == 0:
            n /= i

    return n == 1

# just my intuition, didn't solve the problem
from math import remainder


def isHappy(n:int):
    while n!=1:
        res = 0
        while n:
            remainder = n % 10
            res += remainder * remainder
            n = n // 10
        n = res

    return True

# print(isHappy(19))
# print(isHappy(1))
# print(isHappy(2))

# 2. efficient solution
def isHappy(n:int):
    # set up a hash set, keep track every number that we visited
    visit = set()

    # if n is already in the visit set, means there is an infinite loop
    while n not in visit and n!=1:
        visit.add(n)
        res = 0
        while n:
            remainder = n % 10
            res += remainder * remainder
            n = n // 10
        n = res

    return n == 1

print(isHappy(19))
print(isHappy(1))
print(isHappy(2))


# 3.better version - helper function

class Solution:
    def isHappy(self,n:int)->bool:
        visit = set()
        while n not in visit:
            visit.add(n)

            n = self.sumOfSquares()

            if n ==1:
                return True
        return False

    def sumOfSquares(self, n)->int:
        res = 0
        while n:
            remainder = n % 10
            res += remainder* remainder
            n = n // 10
        return res
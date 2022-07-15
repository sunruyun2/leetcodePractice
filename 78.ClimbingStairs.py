# intuition - dynamic programing
from pickletools import optimize


def climbStairs(n)->int:
    if n == 1:
        return 1
    if n ==2:
        return 2
    op1 , op2 = 1, 2
    # steps = 1
    for num in range(3,n+1):
        temp = op1 +  op2
        op1 = op2
        op2 = temp
    return temp

print(climbStairs(1))
print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))

# take a glance of the code and try to rewrite it
def climbStairs(n):
    opt1 , opt2 = 1,1
    temp =1
    for i in range(n-1):
        temp = opt1
        opt1 = opt2 +opt2
        opt2 = temp
    return opt1
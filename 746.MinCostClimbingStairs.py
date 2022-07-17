# 1.intuition - dynamic programming or recursive function
def minCostClibingStairs(cost:list)->int:
    if len(cost) ==1:
        return 0
    if len(cost) ==1:
        return min(cost)

    op1 , op2 = 0 , 0
    for i in range(2, len(cost)+1):
        steps = min(op1 + cost[i-2], op2 + cost[i-1])
        op1 = op2
        op2 = steps
    return steps


print(minCostClibingStairs([10,15,20]))
print(minCostClibingStairs([1,100,1,1,1,100,1,1,100,1]))
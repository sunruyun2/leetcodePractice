# 1. intuition - O(n), two pointer
def sortedSquares(nums:list)->list:
    l , r = 0 , len(nums) -1
    res = []
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            res.append(nums[l]* nums[l])
            l +=1
        else:
            res.append(nums[r]* nums[r])
            r -=1
    return res[::-1]
    
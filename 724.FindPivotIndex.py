def pivotIndex(nums:list)->int:
    sumOfList = sum(nums)
    for i in range(len(nums)):
        leftSum = sum(nums[:i])
        if (sumOfList - nums[i] )/ 2 == leftSum:
            return i
    return -1

print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([1]))
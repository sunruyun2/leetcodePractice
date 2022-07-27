# 1. how to use binary search
def searchInsert(nums:list, target:int)->int:
    left = 0
    right = len(nums) -1
    while left <= right:
        mid = (left + right) // 2 
        if target > nums[mid]:
            left = mid + 1
        elif target < left:
            right = mid -1
        else:
            return mid

    return left

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))
    

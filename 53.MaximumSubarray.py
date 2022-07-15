# 1.brute force bmw
def MaxSub(nums:list)->int:
    max_num = nums[0]
    for i in range(len(nums)):
        sub_sum = 0
        for j in range(i,len(nums)):
            sub_sum+=nums[j]
            max_num = max(max_num,sub_sum)

    return max_num

# print(MaxSub([-2,1,-3,4,-1,2,1,-5,4]))
# print(MaxSub([1]))
# print(MaxSub([5,4,-1,7,8]))


# 2.kind of like sliding window = remove negative prefix
# time complexity O(n) - Space complexity O(1)
def maxSubArray(nums:list) ->int:
    maxSub = nums[0]
    curSum = 0
    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum +=n
        maxSub = max(curSum , maxSub)
    return maxSub
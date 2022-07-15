def rob(nums:list) ->int:
    rob1,rob2 = 0,0

    # [rob1, rob2, n, n+1] 
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
print(rob([2]))



# fail - I didn't fully understand the question
# it should use dynamic programming method
'''
def rob(nums:list)->int:
    if len(nums) ==1:
        return nums[0]

    odd_house = 0
    odd_sum = 0
    even_house = 1
    even_sum = 0
    while odd_house < len(nums):
        odd_sum+=nums[odd_house]
        odd_house+=2
    while even_house < len(nums):
        even_sum+=nums[even_house]
        even_house+=2
    return max(odd_sum,even_sum)

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
print(rob([2]))
'''
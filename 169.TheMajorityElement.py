# 1.hash map
def majorityElement(nums:list)->int:
    n =  len(nums)
    dict = {}
    for i in nums:
        dict.setdefault(i , 0)
        dict[i] +=1
    for key, value in dict.items():
        if dict[key] > n /2:
            return key

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))



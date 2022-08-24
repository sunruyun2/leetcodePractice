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

# optimize it
def majorityElement(nums:list):
    count = {}
    res , maxCount = 0 , 0
    for i in nums:
        count[i] = count.get(i , 0) + 1
        res = i if count[i] > maxCount else res
        maxCount = max(maxCount , count[i])
    return res

# 3. boyer-moore algorithm, it works when there is always a majority number
def majorityElement(nums:list):
    count = 0
    res = nums[0]
    for n in nums:
        if n == res:
            count +=1
        elif n!=res and count!=0:
            count -=1
        else:
            res = n
            count +=1
    return res


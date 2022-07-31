# 1.tuition, hash set, time limit exceeded
def findLength(nums1:list, nums2:list):
    length = 0
    lengthList = [length]
    numsLength = len(nums1)
    seen = set()
    while length <= numsLength:
        length+=1
        for i in range(numsLength - length +1):
            seen.add(tuple(nums1[i:i+length]))
        
        for i in range(numsLength - length +1):
            if tuple(nums2[i:i+length]) in seen:
                lengthList.append(length)
                break
    return max(lengthList)

# print(findLength([1,2,3,2,1],[3,2,1,4,7]))

# start from the maxLength
def findLength(nums1:list, nums2:list):
    length = len(nums1)
    numsLength = len(nums1)
    while length !=0:
        seen = set()
        for i in range(numsLength - length +1):
            seen.add(tuple(nums1[i:i+length]))
        
        for i in range(numsLength - length +1):
            if tuple(nums2[i:i+length]) in seen:
                return length
        length-=1
    return 0

print(findLength([1,2,3,2,1],[3,2,1,4,7]))
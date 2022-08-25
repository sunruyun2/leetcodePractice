# 1.intuition - brute force
def nextGreaterElement(nums1:list, nums2:list)->list:
    res = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                index = j + 1
                break
        while index < len(nums2):
            if nums2[index] > nums2[j]:
                res.append(nums2[index])
                break
            index+=1
        if len(res) -1 != i:
            res.append(-1)
    return res

nums1 = [4,1,2]
nums2 = [1,3,4,2]

nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1 , nums2))


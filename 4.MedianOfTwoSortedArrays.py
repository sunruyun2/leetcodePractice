# tuition: iterate two array and form a new sorted array and calculate the median of the new array
# second thought: don't have to iterate two array?
def findMedianSortedArrays(nums1, nums2)->float:
    i , j = 0 , 0
    newArr = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            newArr.append(nums1[i])
            i+=1
        else:
            newArr.append(nums2[j])
            j+=1
    
    if i != len(nums1):
        newArr += nums1[i:]
    elif j != len(nums2):
        newArr += nums2[j:]

    if len(newArr) % 2 == 1:
        return newArr[len(newArr)//2]
    return (newArr[len(newArr) // 2] + newArr[len(newArr) // 2 -1])/2
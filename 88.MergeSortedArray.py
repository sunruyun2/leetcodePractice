# 1.two pointer -intuitive -bmo
def merge(nums1:list,m:int,nums2:list,n:int)->None:
    new_list = []
    i , j = 0 , 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            new_list.append(nums1[i])
            i+=1
        else:
            new_list.append(nums2[j])
            j+=1

    if i < m:
        new_list = new_list + nums1[i:m]
    elif j < n:
        new_list = new_list + nums2[j:]
    
    for i in range(len(new_list)):
        nums1[i] = new_list[i]

    return nums1

print(merge([1,2,3,0,0,0],3,[2,5,6],3))
print(merge([1],1,[],0))
print(merge([0],0,[1],1))


# 2.I don't know when I write this
def solution2(nums1, m,nums2,n):
        copyNums1 = []
        pointer1 = 0
        pointer2 = 0
        for i in range(len(nums1)):
            if pointer1 >= m:
                copyNums1.append(nums2[pointer2])
                pointer2+=1 
            elif pointer2 >=n:
                copyNums1.append(nums1[pointer1])
                pointer1+=1
            elif nums1[pointer1] < nums2[pointer2]:
                copyNums1.append(nums1[pointer1])
                pointer1+=1
            else:
                copyNums1.append(nums2[pointer2])
                pointer2+=1

        for i in range(len(nums1)):
            nums1[i] = copyNums1[i]

        return copyNums1



# 2. optimal - in-place solution without extra memory - merge from the end of the list
def merge(nums1, m, nums2, n):
    # last index nums1
    last = m + n -1

    # merge in reverse order
    while m>0 and n>0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -=1
        else:
            nums1[last] = nums2[n-1]
            n-=1
        last -=1

    # fill nums1 with leftover nums2 elements
    while n:
        nums1[last] = nums2[n-1]
        last -=1
        n -=1


print(merge([1,2,3,0,0,0],3,[2,5,6],3))
print(merge([1],1,[],0))
print(merge([0],0,[1],1))
    
        
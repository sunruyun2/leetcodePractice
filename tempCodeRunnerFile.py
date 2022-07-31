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
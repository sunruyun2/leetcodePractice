# 1.tuition, detect the nums you have seen, time limit exceeded, O(n^2), also i j works in this way
def containsDuplicate(nums:list[int])->bool:
    seen = []
    for a in nums:
        if a in seen:
            return True
        else:
            seen.append(a)
    return False

# 2.sort function - accepted


# 3.optimal - hash set
def containDuplicate(nums:list[int])->bool:
    seen = set()
    for a in nums:
        if a in seen:
            return True
        else:
            seen.add(a)
    return False
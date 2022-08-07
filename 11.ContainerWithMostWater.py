# 1.brute force
# time complexity - O(n^2)
def maxArea(height:list[int])->int:
    res = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            res = max (res , min (height[i] , height[j]) * (j - i) )

    return res

# print(maxArea([1,8,6,2,5,4,8,3,7]))
# print(maxArea([1,1]))

# 2.Solution - two pointers - O(n )
def maxArea(height:list[int])->int:
    area = 0
    l, r = 0 , len(height) -1
    while l < r:
        area = max (area , min (height[l] , height[r]) * (r - l) )
        if height[l] > height[r]:
            r -=1
        else:
            l +=1
    return area

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
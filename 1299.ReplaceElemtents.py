# 1. brute force, very straight forward
# T - O(n * b) S - O(1)
def replaceElement(arr:list)->list:
    if len(arr) == 1:
        return [-1]

    for i in range(len(arr)):
        max = -1
        for j in range(i+1, len(arr)):
            if arr[j] > max:
                max = arr[j]
        arr[i] = max

    return arr

print(replaceElement([17,18,5,4,6,1]))
print(replaceElement([400]))


# 2. optimal solution
# start from the end of the array -
# T - O(n) S - O(n)
def replaceElement(arr:list)->list:
    if len(arr) == 1:
        return [-1]

    return_arr = arr.copy()
    for i in range(len(arr)-2 , -1 , -1):
        return_arr[i] = max(arr[i+1], return_arr[i+1])

    return_arr[-1] = -1

    return return_arr

print(replaceElement([17,18,5,4,6,1]))
print(replaceElement([400]))


# 3.the real optimal solution

def replaceElement(arr:list) ->list:
    rightMax = -1

    #attention: reverse the list, the range of range funciton 
    for i in range(len(arr) -1 , -1, -1):
        newMax = max( arr[i] , rightMax)
        arr[i] = rightMax
        rightMax = newMax
    return arr

print(replaceElement([17,18,5,4,6,1]))
print(replaceElement([400]))
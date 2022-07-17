# 1. brute force, very straight forward
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

# 1. two pointers - bmo
def twoSum(numbers:list,target:int)->list:
    i = 0
    j = len(numbers) -1
    sum = numbers[i] + numbers[j]
    while sum != target:
        if sum < target:
            i +=1
        else:
            j -=1
        sum = numbers[i] + numbers[j]
    return [i+1,j+1]

print(twoSum([2,7,11,15],9))
print(twoSum([2,3,4],6))
print(twoSum([-1,0],-1))

# didn't test, just memory
from re import I


def brute_force(list,target):
    for i in range(list):
        for j in range(i+1,list):
            if list[j] + list[i] == target:
                return i,j


def hash_map_two_sum(arr, target):
    prevMap = {} #val : index
    for i, n in range(len(arr)):
        diff = target - n
        if diff in prevMap.keys():
            return [i, prevMap[diff]]
        prevMap[n] = i
    return
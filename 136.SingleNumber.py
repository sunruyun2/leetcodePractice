# intuition - hash table
import ntpath


def singleNumber(nums:list)->int:
    table = {}
    for num in nums:
        table.setdefault(num , 0)
        table[num] += 1
    for num in table.keys():
        if table[num] == 1:
            return num
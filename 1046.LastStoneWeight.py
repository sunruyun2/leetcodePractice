# 1. brute force
import heapq


def lastStoneWeight(stones:list)->int:
    while len(stones) >1:
        stones.sort()
        leftWeight = stones[-1] - stones[-2]
        stones.pop()
        stones.pop()
        if leftWeight:
            stones.append(leftWeight)

    if stones:
        return stones[0]
    else:
        return 0

# print(lastStoneWeight([2,7,4,1,8,1]))
# print(lastStoneWeight([1]))
# print(lastStoneWeight([2,2,2,2]))

# 2. use heap(max heap)
def lastStoneWeight(stones:list)->int:
    sontes = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if first != second:
            heapq.heappush(stones, second - first)
    
    # catch edge case where the list is empty - clever
    stones.append(0)
    return abs(stones[0])
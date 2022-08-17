# 1. intuition: define a class, binary search
# 
import heapq


class KthLargest:
    def __init__(self, k:int, nums:list[int]) -> None:
        self.nums = nums
        self.nums.sort()
        self.k = k

    def add(self, val:int)->int:

        def binarysearch(val):
            l , r = 0 , len(self.nums)
            while l < r:
                mid = l + (r -l) // 2
                if val <= self.nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            return l
                    
        self.nums.insert(binarysearch(val), val)

        return self.nums[-self.k]

# my_list = KthLargest(3, [4,5,8,2])
# print(my_list.add(3))
# print(my_list.add(5))
# print(my_list.add(10))
# print(my_list.add(9))
# print(my_list.add(4))

# my_list = KthLargest(1, [])
# print(my_list.add(-3))
# print(my_list.add(-2))
# print(my_list.add(-4))
# print(my_list.add(0))
# print(my_list.add(4))

# 2.min heap
class KthLargest:
    def __init__(self, k:int, nums:list[int]) -> None:
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val:int)->int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# try to define it by my own - practice
class KthLargest:
    def __init__(self, k:int, nums:list[int]) -> None:
        self.minHeap , self.k = nums, k
        heapq.heapify(self.minHeap)
        while k < len(self.minHeap):
            heapq.heappop(self.minHeap)


    def add(self, val:int)->int:
        heapq.heappush(val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        
        heapq.heapify(nums)
        remove = len(nums) - k 
        for i in range(remove):
            heapq.heappop(nums)
            
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]
        

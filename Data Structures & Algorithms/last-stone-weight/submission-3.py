class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_sort = [-stone for stone in stones]
        heapq.heapify(max_sort)
        while (len(max_sort) > 1):
            x = heapq.heappop(max_sort)
            y = heapq.heappop(max_sort)
            if x < y:
                z = x - y
                heapq.heappush(max_sort, z)
        max_sort.append(0)
        return abs(max_sort[0])
        
           


        
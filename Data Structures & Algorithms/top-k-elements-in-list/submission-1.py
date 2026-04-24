class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = Counter(nums)
        top_k = heapq.nlargest(k, frequencyMap.keys(), key = frequencyMap.get)
        return top_k
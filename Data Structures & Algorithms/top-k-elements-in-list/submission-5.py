class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums) + 1
        buckets = [[] for _ in range(n)]
        # [
        #     [],
        #     [],
        #     [],
        #     [],
        #     [],
        #     [],
        #     []

        # ]

        # nums=[1,2,2,3,3,3]
        # 0 sampe 7

        dictionary_nums = Counter(nums) 

        # dictionary_nums = {
        #     1: 3,
        #     2: 2,
        #     3: 1
        # }

        for num, cnt in dictionary_nums.items():
            buckets[cnt].append(num)
        
        res = []
        # Return the number that is k most
        for i in range(len(buckets) - 1,0,-1):
            for num in buckets[i]:
                res.append(num)
                
                if len(res) == k:
                    return res

        
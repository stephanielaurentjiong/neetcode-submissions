class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        dictionary_nums = Counter(nums)
        sorted_names = sorted(dictionary_nums, key = lambda x: dictionary_nums[x], reverse=True)

        print(sorted_names)

        for key in sorted_names:
            if k != 0:
                result.append(key)
                k -= 1
        
        return result
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            left = target - num
            if left not in dictionary.keys():
                dictionary[num] = i
            else:
                return [dictionary.get(left), i]
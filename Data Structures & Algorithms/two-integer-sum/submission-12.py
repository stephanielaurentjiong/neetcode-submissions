class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            nums_left = target-nums[i]
            if (nums_left) not in nums_dict:
                nums_dict[nums[i]] = i
            else:
                return[nums_dict[nums_left], i]

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNum = set(nums)
        n = len(nums)
        return len(setNum) != n
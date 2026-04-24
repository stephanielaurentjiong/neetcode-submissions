class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # Step 1: Sort the array

        # Step 2: Check adjacent elements
        for i in range(len(nums) - 1):  
            if nums[i] == nums[i + 1]:  
                return True  # Duplicate found

        return False  # No duplicates
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest = 0 #To be returned the max consequtive sequence

        # Iterate over the nums list
        # For each element check if the previous num is in set
        # If not put that into the hashSet as the head --> continue looking
        # at the consequtive sequence in the nums list
        
        for num in nums:
            if (num - 1) not in nums_set:
                length = 0 #Start from the head with length 1
                while (num + length) in nums_set:
                    print("num + length :" , num + length)
                    length += 1
                longest = max(length, longest)
        return longest


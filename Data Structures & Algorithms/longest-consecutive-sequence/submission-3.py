class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hashset = set(nums)
        print(nums_hashset)
        start = 0
        length = 0
        max_length = 0
        
        for num in nums_hashset:

            if num - 1 not in nums_hashset:
                start = num
                length = 1

                while start + 1 in nums_hashset:
                    start += 1 
                    length += 1

                max_length = max(length, max_length)
            
            
        return max_length
        
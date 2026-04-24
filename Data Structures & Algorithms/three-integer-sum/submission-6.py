class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
       
        for i in range(len(nums)):
            # Skip the A pointer duplicate
            if i != 0 and nums[i] == nums[i -1]:
                continue

            A = i
            L = i + 1
            R = len(nums) - 1
            
            while L < R:
                total = nums[L] + nums[R] + nums[A]
                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
                else:
                    
                    result.append([nums[A], nums[L], nums[R]])
    
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1

                    L += 1
                    R -= 1
            
        return result
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)

        for i in range(length):
            multiplication = 1;
            for index, value in enumerate(nums):
                if i != index:
                    multiplication = multiplication * value
            res.append(multiplication)    
        return res
             
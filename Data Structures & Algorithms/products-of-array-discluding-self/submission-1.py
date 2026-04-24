class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []

        multiplication = 1
        for i in range(len(nums)):
            if (i != 0):
                multiplication *= nums[i - 1]
                prefix.append(multiplication)
            else:
                prefix.append(multiplication)
     

        
        print(f"Prefix: {prefix}")
        suffix = []

        multiplication2 = 1
        for i in range(len(nums) - 1, -1, -1 ):
            if (i != len(nums) - 1):
                multiplication2 *= nums[i + 1]
                suffix.insert(0, multiplication2)  
            else:
                suffix.insert(len(nums) - 1, 1)  

        
        print(f"Suffix: {suffix}")
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result

        
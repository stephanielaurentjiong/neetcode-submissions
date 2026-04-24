class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        print(zero_count)

        total = 1
        for num in nums:
            if num != 0:
                total *= num
            
        output = []
        
        if zero_count == 1:
            for num in nums:
                if num != 0:
                    output.append(0)
                else:
                    output.append(total)
        
        elif zero_count == 0:
            for num in nums:
                res = total // num
                output.append(res)
        else:
            for num in nums:
                output.append(0)
        

        return output

        
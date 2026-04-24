class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use hashmap, key the element, value the index
        result = {}

        # Loop over the element AND index
        for i, num in enumerate(nums):
            print(result)
            # Find the sisa after substraction
            sisa = target - num

            # If it is in hashmp, then return the index of the element
            if sisa in result:
                return[result[sisa], i]

            # If the sisa is not in the hashmap, we put that number as a placeholder
            else:
                
                result[num] = i

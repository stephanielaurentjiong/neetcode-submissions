class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_water = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            # find the min height
            min_height = min(heights[left], heights[right])
            width = right - left
            max_water = max(max_water, min_height * width)

            if heights[left] < heights[right] :
                left += 1
            else:
                right -= 1
        
        return max_water
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        left = 0;
        right = len(heights) - 1

        while left < right:
            #Find the height (to determine smaller pointer, move inwards)
            height = min(heights[left], heights[right])

            #Find the width
            width = right - left

            #Find the max water (get the height bottleneck * width)
            max_water = max(max_water, height * width)

            #Move pointer
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water
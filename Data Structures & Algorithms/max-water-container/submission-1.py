class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = (right - left) * min(heights[left], heights[right])
        while left < right:
            if heights[left] < heights[right]:
                initial_left = left
                left += 1
                while left < right and heights[initial_left] > heights[left]:
                    left += 1
                max_area = max(max_area, (right - left) * min(heights[left], heights[right]))
            else:
                initial_right = right
                right -= 1
                while left < right and heights[initial_right] > heights[right]:
                    right -= 1
                max_area = max(max_area, (right - left) * min(heights[left], heights[right]))
        return max_area
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for right, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                rect_h = heights[stack.pop()]
                left = 0 if not stack else stack[-1] + 1
                max_area = max(max_area, rect_h * (right - left))
            stack.append(right)
        while stack:
            rect_h = heights[stack.pop()]
            left = 0 if not stack else stack[-1] + 1
            max_area = max(max_area, rect_h * (len(heights) - left))
        return max_area

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        ascending_stack = []
        for ind, h in enumerate(heights):
            while ascending_stack and heights[ascending_stack[-1]] > h:
                highest_unsolved_h = heights[ascending_stack.pop()]
                index_second_highest_h = 0 if not ascending_stack else ascending_stack[-1] + 1
                max_area = max(max_area, highest_unsolved_h * (ind - index_second_highest_h))
            ascending_stack.append(ind)
        while ascending_stack:
            highest_unsolved_h = heights[ascending_stack.pop()]
            index_second_highest_h = 0 if not ascending_stack else ascending_stack[-1] + 1
            max_area = max(max_area, highest_unsolved_h * (len(heights) - index_second_highest_h))
        return max_area

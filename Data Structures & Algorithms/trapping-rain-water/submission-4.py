class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right] 
        accumulate = 0
        while left < right:
            if left_max <= right_max:
                accumulate += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                accumulate += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return accumulate
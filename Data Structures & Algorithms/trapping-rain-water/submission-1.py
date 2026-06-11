class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        accumulate = 0
        while left < right:
            if height[left] <= height[right]:
                m = height[left]
                left += 1
                if left == right:
                    return accumulate
                while height[left] < m:
                    accumulate += m - height[left]
                    left += 1
            else:
                m = height[right]
                right -= 1
                if left == right:
                    return accumulate
                while height[right] < m:
                    accumulate += m - height[right]
                    right -= 1
        return accumulate
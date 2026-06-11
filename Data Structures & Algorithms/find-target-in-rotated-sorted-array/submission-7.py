class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[mid] >= nums[right] and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] < nums[right] and nums[right] < target:
                    right = mid
                else:
                    left = mid + 1
        return -1

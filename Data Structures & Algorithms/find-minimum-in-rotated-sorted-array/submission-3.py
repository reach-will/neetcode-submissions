class Solution:
    def findMin(self, nums: List[int]) -> int:
        last = nums[-1]

        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= last:
                right = mid
            else:
                left = mid + 1

        return nums[left]
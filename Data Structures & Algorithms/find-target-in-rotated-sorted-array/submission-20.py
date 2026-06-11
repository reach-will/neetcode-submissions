class Solution:
    def sorted_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        first = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= first:
                if first <= target <= nums[mid]:
                    return self.sorted_search(nums, target, left, mid - 1)
                else:
                    left = mid + 1
            else:
                if nums[right] >= target >= nums[mid]:
                    return self.sorted_search(nums, target, mid + 1, right)
                else:
                    right = mid - 1
        return -1

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
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target:
                    if nums[mid] > target:
                        return self.sorted_search(nums, target, left, mid)
                    else:
                        left = mid + 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target:
                    if nums[mid] < target:
                        return self.sorted_search(nums, target, mid + 1, right)
                    else:
                        right = mid
                else:
                    right = mid
        return -1

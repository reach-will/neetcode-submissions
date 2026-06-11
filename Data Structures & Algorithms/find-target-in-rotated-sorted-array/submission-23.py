class Solution:
    def sorted_search(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search(self, nums, target):
        first = nums[0]
        target_in_left = target >= first

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= first:
                if target_in_left and target <= nums[mid]:
                    return self.sorted_search(nums, target, left, mid - 1)
                left = mid + 1
            else:
                if not target_in_left and target >= nums[mid]:
                    return self.sorted_search(nums, target, mid + 1, right)
                right = mid - 1

        return -1
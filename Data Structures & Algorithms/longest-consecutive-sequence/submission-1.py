class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        bounds = {}
        m = 1
        for num in nums:
            if num in bounds:
                continue
            if num - 1 in bounds and bounds[num - 1] <= num - 1 and bounds[bounds[num - 1]] <= num - 1 and num + 1 in bounds and bounds[num + 1] >= num + 1 and bounds[bounds[num + 1]] >= num + 1:
                left = bounds[num - 1]
                right = bounds[num + 1]
                bounds[left] = right
                bounds[right] = left
                m = max(m, right - left + 1)
                continue
            if num - 1 in bounds and bounds[num - 1] <= num - 1 and bounds[bounds[num - 1]] <= num - 1:
                bounds[num] = bounds[num - 1]
                bounds[bounds[num]] += 1
                m = max(m, bounds[bounds[num]] - bounds[num] + 1)
                continue
            if num + 1 in bounds and bounds[num + 1] >= num + 1 and bounds[bounds[num + 1]] >= num + 1:
                print(num, bounds)
                bounds[num] = bounds[num + 1]
                bounds[bounds[num]] -= 1
                m = max(m, bounds[num] - bounds[bounds[num]] + 1)
                print(bounds)
                continue
            bounds[num] = num
        return m
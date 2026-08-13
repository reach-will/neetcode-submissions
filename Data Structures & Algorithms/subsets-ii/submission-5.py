class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start):
            result.append(path[:])

            if start == len(nums):
                return

            path.append(nums[start])
            backtrack(start + 1)
            path.pop()

            for i in range(start + 1, len(nums)):
                if nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        path = []
        backtrack(0)
        return result
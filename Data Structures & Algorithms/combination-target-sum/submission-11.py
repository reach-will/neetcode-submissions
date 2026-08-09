class Solution:
    def backtrack(self, start: int, remaining: int) -> None:
        if remaining == 0:
            self.ans.append(self.path[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(self.nums)):
            self.path.append(self.nums[i])
            self.backtrack(i, remaining - self.nums[i])
            self.path.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.path = []
        self.ans = []
        self.backtrack(0, target)
        return self.ans

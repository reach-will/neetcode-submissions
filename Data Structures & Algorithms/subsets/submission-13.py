class Solution:
    def backtrack(self, start: int) -> None:
        if start == len(self.nums):
            self.ans.append(self.path[:])
            return

        self.path.append(self.nums[start])
        self.backtrack(start + 1)
        self.path.pop()
        self.backtrack(start + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.path = []
        self.ans = []
        self.backtrack(0)
        return self.ans
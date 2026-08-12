class Solution:
    def backtrack(self, start: int) -> None:
        if start == len(self.nums):
            self.result.append(self.path[:])
            return
        i = start
        e = self.nums[i]
        while i < len(self.nums) and self.nums[i] == e:
            i += 1
        self.backtrack(i)
        for j in range(start, i):
            self.path.append(e)
            self.backtrack(i)
        del self.path[-(i - start):]
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.path = []
        self.result = []
        self.backtrack(0)
        return self.result
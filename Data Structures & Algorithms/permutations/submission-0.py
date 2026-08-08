class Solution:
    def backtrack(self):
        if len(self.pool) == 0:
            self.ans.append(self.path[:])
            return

        for i in range(len(self.pool)):
            self.path.append(self.pool.pop(i))
            self.backtrack()
            self.pool.insert(i, self.path.pop())

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        self.nums = nums
        self.path = []
        self.pool = nums[:]
        self.backtrack()
        return self.ans

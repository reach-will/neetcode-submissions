class Solution:
    def backtrack(self, start: int):
        if start == len(self.path):
            self.ans.append(self.path[:])
            return

        self.backtrack(start + 1)
        for i in range(start + 1, len(self.path)):
            self.path[start], self.path[i] = self.path[i], self.path[start]
            self.backtrack(start + 1)
            self.path[start], self.path[i] = self.path[i], self.path[start]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.path = nums
        self.backtrack(0)
        return self.ans

class Solution:
    def backtrack(self, start: int) -> None:
        if start == len(self.nums):
            self.result.append(self.path[:])
            return

        curr_num = self.nums[start]

        i = start + 1
        while i < len(self.nums) and self.nums[i] == curr_num:
            i += 1

        self.backtrack(i)
        for _ in range(start, i):
            self.path.append(curr_num)
            self.backtrack(i)
        del self.path[-(i - start):]

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.path = []
        self.result = []
        self.backtrack(0)
        return self.result

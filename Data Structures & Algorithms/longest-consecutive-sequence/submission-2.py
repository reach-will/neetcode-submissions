class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = Counter()
        res = 0

        for num in nums:
            if not c[num]:
                c[num] = c[num - 1] + c[num + 1] + 1
                c[num - c[num - 1]] = c[num]
                c[num + c[num + 1]] = c[num]
                res = max(res, c[num])
        return res
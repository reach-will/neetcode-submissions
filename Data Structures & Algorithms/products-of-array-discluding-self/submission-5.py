class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = n * [1]
        pre = nums[0]
        suf = nums[-1]
        for i in range(1, n):
            res[i] = pre
            pre *= nums[i]
        for i in range(n - 2, -1, -1):
            res[i] *= suf
            suf *= nums[i]
        return res
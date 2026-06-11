class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [1]
        prefix_prod = [1] * n
        for i, num in enumerate(nums[:-1]):
            prefix_prod[i + 1] = prefix_prod[i] * num
        suffix_prod = [1] * n
        for i, num in enumerate(reversed(nums[1:])):
            suffix_prod[n - i - 2] = suffix_prod[n - i - 1] * num
        return [p * s for p, s in zip(prefix_prod, suffix_prod)]
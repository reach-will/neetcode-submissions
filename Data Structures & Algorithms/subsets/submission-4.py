class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            subsets += [subset + [n] for subset in subsets]
        return subsets
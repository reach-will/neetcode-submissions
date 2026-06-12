class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            sub = []
            for subset in subsets:
                sub.append(subset)
                sub.append(subset + [n])
            subsets = sub
        return subsets
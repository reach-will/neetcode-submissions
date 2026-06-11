class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i, n in enumerate(nums):
            if target - n in numToIndex:
                return [numToIndex[target - n], i]
            numToIndex[n] = i
        return [-1, -1]
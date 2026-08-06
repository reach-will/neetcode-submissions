class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        combinations = []
        nums.sort()
        for n in nums:
            if n < target:
                combinations.append([n])
                continue
            if n == target:
                ans.append([n])
            break
        while combinations:
            new_combinations = []
            for c in combinations:
                for n in nums:
                    if c[-1] > n:
                        continue
                    if sum(c) + n < target:
                        new_combinations.append(c + [n])
                        continue
                    if sum(c) + n == target:
                        ans.append(c + [n])
                    break
            combinations = new_combinations
        return ans
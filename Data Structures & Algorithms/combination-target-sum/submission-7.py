class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        stack = []
        nums.sort()
        num_to_index = {n:i for i,n in enumerate(nums)}
        for n in nums:
            if n < target:
                stack.append(([n], n))
                continue
            if n == target:
                ans.append([n])
            break
        while stack:
            new_stack = []
            for combination, total in stack:
                start_index = num_to_index[combination[-1]]
                for n in nums[start_index:]:
                    if total + n < target:
                        new_stack.append((combination + [n], total + n))
                        continue
                    if total + n == target:
                        ans.append(combination + [n])
                    break
            stack = new_stack
        return ans
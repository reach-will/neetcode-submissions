class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        triplet_set = set()
        num_to_indices = defaultdict(list)
        for i, n in enumerate(nums):
            num_to_indices[n].append(i)

        for i, n in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num_to_indices[- n - nums[j]] and num_to_indices[- n - nums[j]][-1] > j and frozenset({n, nums[j], - n - nums[j]}) not in triplet_set:
                    ans.append([n, nums[j], - n - nums[j]])
                    triplet_set.add(frozenset({n, nums[j], - n - nums[j]}))
        return ans
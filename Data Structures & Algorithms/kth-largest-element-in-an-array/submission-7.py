class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums) / 2:
            return heapq.nlargest(k, nums)[-1]
        else:
            return heapq.nsmallest(len(nums) - k + 1, nums)[-1]
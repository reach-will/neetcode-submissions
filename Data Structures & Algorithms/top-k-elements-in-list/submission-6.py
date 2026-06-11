class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return sorted(counts, key=counts.get, reverse=True)[:k]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [e[0] for e in Counter(nums).most_common(k)]
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            remainder = heapq.heappop_max(stones) - heapq.heappop_max(stones)

            if remainder != 0:
                heapq.heappush_max(stones, remainder)

        return stones[0] if stones else 0

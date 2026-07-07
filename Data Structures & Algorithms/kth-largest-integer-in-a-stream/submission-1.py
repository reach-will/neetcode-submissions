class KthLargest:
    k = 0

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [float("-inf")] + nums[:k-1]
        heapq.heapify(self.heap)
        for n in nums[k-1:]:
            heapq.heappush(self.heap, max(n, heapq.heappop(self.heap)))

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, max(val, heapq.heappop(self.heap)))
        return self.heap[0]

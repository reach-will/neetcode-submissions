class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [float("-inf")] + nums[:k-1]
        heapq.heapify(self.heap)
        for n in nums[k-1:]:
            heapq.heappushpop(self.heap, n)

    def add(self, val: int) -> int:
        heapq.heappushpop(self.heap, val)
        return self.heap[0]

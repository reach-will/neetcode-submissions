class KthLargest:
    k = 0

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:k-1]
        heapq.heapify(self.heap)
        self.kth = float("-inf")
        for n in nums[k-1:]:
            if n <= self.kth:
                continue
            heapq.heappush(self.heap, n)
            self.kth = heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if val <= self.kth:
            return self.kth
        heapq.heappush(self.heap, val)
        self.kth = heapq.heappop(self.heap)
        return self.kth

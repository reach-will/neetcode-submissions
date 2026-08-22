class MedianFinder:

    def __init__(self):
        self.lower_half = [float('-inf')]
        self.upper_half = [float('inf')]

    def addNum(self, num: int) -> None:
        if len(self.lower_half) > len(self.upper_half):
            if num >= self.lower_half[0]:
                heapq.heappush(self.upper_half, num)
                return

            new_upper_median = heapq.heappushpop_max(self.lower_half, num)
            heapq.heappush(self.upper_half, new_upper_median)
            return

        if num <= self.lower_half[0]:
            heapq.heappush_max(self.lower_half, num)
            return

        new_lower_median = heapq.heappushpop(self.upper_half, num)
        heapq.heappush_max(self.lower_half, new_lower_median)

    def findMedian(self) -> float:
        if len(self.lower_half) > len(self.upper_half):
            return self.lower_half[0]

        return (self.lower_half[0] + self.upper_half[0]) / 2

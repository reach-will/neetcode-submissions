class MedianFinder:

    def __init__(self):
        self.is_sorted = False
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        if len(self.nums) >= 2 and self.nums[-2] > self.nums[-1]:
            self.is_sorted = False

    def findMedian(self) -> float:
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True
        return self.nums[len(self.nums) // 2] if len(self.nums) % 2 == 1 else (self.nums[len(self.nums) // 2 - 1] + self.nums[len(self.nums) // 2]) / 2
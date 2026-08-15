class Solution:
    def euclideanDistanceOrigin(self, points: List[int]) -> float:
        return math.sqrt(points[0] * points[0] + points[1] * points[1])
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key = self.euclideanDistanceOrigin)
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map[key]

        if not values:
            return ""
    
        left, right = 0, len(values) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if values[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid
        return values[left][0] if values[left][1] <= timestamp else ""

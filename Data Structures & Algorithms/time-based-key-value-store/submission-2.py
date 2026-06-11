class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map[key]

        if not values:
            return ""
    
        left, right = 0, len(values)
        while left < right:
            mid = (left + right) // 2
            if values[mid][1] > timestamp:
                right = mid
            else:
                left = mid + 1
        return values[left - 1][0] if left > 0 and values[left - 1][1] <= timestamp else ""

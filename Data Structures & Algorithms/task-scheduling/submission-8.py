class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        max_count = -1
        repeated_max_count = 0
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
            count = counts[ord(task) - ord('A')]
            if count > max_count:
                max_count = count
                repeated_max_count = 1
                continue

            if count == max_count:
                repeated_max_count += 1

        time = (max_count - 1) * (n + 1) + repeated_max_count
        return max(len(tasks), time)

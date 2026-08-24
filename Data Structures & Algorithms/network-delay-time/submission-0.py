class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))

        priority_queue = [(0, k)]
        visit = set()
        t = 0
        while priority_queue:
            w1, n1 = heapq.heappop(priority_queue)
            if n1 in visit:
                continue

            visit.add(n1)
            t = w1

            for n2, w2 in adj_list[n1]:
                if n2 not in visit:
                    heapq.heappush(priority_queue, (w1 + w2, n2))

        return t if len(visit) == n else -1

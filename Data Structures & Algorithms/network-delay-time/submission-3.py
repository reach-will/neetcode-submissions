class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for source_node, target_node, travel_time in times:
            adj_list[source_node].append((target_node, travel_time))

        visited_nodes = set()
        exploration_time = 0
        pq = [(0, k)]
        while pq:
            traveled_time, node = heapq.heappop(pq)

            if node in visited_nodes:
                continue

            visited_nodes.add(node)
            exploration_time = traveled_time

            for neighbor_node, next_neighbor_travel_time in adj_list[node]:
                if neighbor_node in visited_nodes:
                    continue

                heapq.heappush(pq, (exploration_time + next_neighbor_travel_time, neighbor_node))

        return exploration_time if len(visited_nodes) == n else -1
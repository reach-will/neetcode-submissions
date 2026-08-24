class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        def dfs(node: int):
            visited.add(node)
            for nei in adj_list[node]:
                if nei in visited:
                    continue

                dfs(nei)

        res = 0
        for node in range(n):
            if node in visited:
                continue

            visited.add(node)
            dfs(node)
            res += 1

        return res

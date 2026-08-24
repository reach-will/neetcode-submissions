class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        visited = set()
        def dfs(node: int, parent: int):
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited:
                    return False

                dfs(neighbor, node)

            return True

        return dfs(0, None) and len(visited) == n

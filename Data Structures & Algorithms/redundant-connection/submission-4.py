class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.ranks = [0] * n
    
    def find(self, u: int):
        if self.parents[u] == u:
            return u

        self.parents[u] = self.find(self.parents[self.parents[u]])
        return self.parents[u]
    
    def union(self, u: int, v: int):
        root_u, root_v = self.find(u), self.find(v)

        if root_u == root_v:
            return False

        if self.ranks[root_u] < self.ranks[root_v]:
            root_u, root_v = root_v, root_u

        if self.ranks[root_u] == self.ranks[root_v]:
            self.ranks[root_u] += 1

        self.parents[root_v] = root_u
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_nodes = len(edges)
        dsu = DSU(num_nodes)

        for u, v in edges:
            if not dsu.union(u - 1, v - 1):
                return [u, v]

        return []

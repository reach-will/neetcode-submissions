class Solution:
    def dfs(self, node):
        for c in self.course_adj_list[node]:
            if c in self.visited:
                return False
            self.visited.add(c)
            if not self.dfs(c):
                return False
            self.visited.remove(c)
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.course_adj_list = defaultdict(list)
        for p in prerequisites:
            self.course_adj_list[p[0]].append(p[1])
        self.visited = set()
        for i in range(numCourses):
            if not self.dfs(i):
                return False
        return True
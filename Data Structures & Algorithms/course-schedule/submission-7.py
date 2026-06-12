class Solution:
    def dfs(self, node):
        if node in self.valid:
            return True

        if node in self.visiting:
            return False

        self.visiting.add(node)

        for c in self.course_adj_list[node]:
            if not self.dfs(c):
                return False

        self.visiting.remove(node)
        self.valid.add(node)
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.course_adj_list = defaultdict(list)
        for p in prerequisites:
            self.course_adj_list[p[0]].append(p[1])

        self.visiting = set()
        self.valid = set()
        for i in range(numCourses):
            if i not in self.valid and not self.dfs(i):
                return False

        return True
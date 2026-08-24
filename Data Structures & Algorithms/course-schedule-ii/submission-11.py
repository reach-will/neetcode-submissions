class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_adj_list = defaultdict(list)
        for p in prerequisites:
            course_adj_list[p[0]].append(p[1])

        ans = []
        visiting = set()
        finishable = set()
        def dfs(node):
            if node in finishable:
                return True

            if node in visiting:
                return False

            visiting.add(node)

            for c in course_adj_list[node]:
                if not dfs(c):
                    return False

            visiting.remove(node)
            finishable.add(node)
            ans.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return ans
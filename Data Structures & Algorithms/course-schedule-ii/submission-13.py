class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: list[list[int]],
    ) -> list[int]:

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        order = []

        def dfs(crs):
            if crs in visiting:
                return False

            # Already fully processed and added to order
            if preMap[crs] is None:
                return True

            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)

            # Fully processed
            preMap[crs] = None
            order.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return order
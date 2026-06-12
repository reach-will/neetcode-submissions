class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_adj_list = defaultdict(list)
        for p in prerequisites:
            prereq_adj_list[p[0]].append(p[1])
        
        visiting = set()
        valid = set()
        ans = []
        def dfs(node):
            if node in valid: return True
            if node in visiting: return False
            
            visiting.add(node)
            for p in prereq_adj_list[node]:
                if not dfs(p):
                    return False
            
            visiting.remove(node)
            valid.add(node)
            ans.append(node)
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return []
        return ans
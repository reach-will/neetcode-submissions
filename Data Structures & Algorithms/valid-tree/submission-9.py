class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # do we just have to check for cycles? 
        # visited set should be n length 
        # there should be no cycles 
        # we can just do dfs once visit all then if the set isnt complete or
        # there is a cycle we return False
        # If we encounter any already visited node that is not the parent of the current node, we return false as it indicates a cycle

        adj = {}
        for x, y in edges:
            if x in adj:
                adj[x].append(y)
            else:
                adj[x] = [y]
            if y in adj:
                adj[y].append(x)
            else:
                adj[y] = [x]

        items = set()
        currentparent = 0

        visited = set() # 0 is not visited 1 is visiting 2 is already visited

        def dfs(x, currentparent):
            
            visited.add(x) if x not in visited else None

            for nei in adj.get(x, []):
                if nei in visited and currentparent == nei:
                    # this means we dont have to visit it but we need to check if its the parent or not
                    continue
                elif nei in visited and currentparent != nei:
                    return False
                

                if not dfs(nei, x):
                    return False
            
            
            return True
        
        if not dfs(0, -1):
            return False
        elif len(visited) != n:
            return False
        return True



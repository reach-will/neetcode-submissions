class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        def dfs(x, y):
            if x < 0 or y < 0 or x >= M or y >= N or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
        ans = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
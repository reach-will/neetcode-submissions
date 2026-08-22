class Solution:
    def dfs(self, grid: List[List[int]], x: int, y: int) -> int:
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 1:
            return

        grid[x][y] = 0
        self.area += 1

        self.dfs(grid, x+1, y)
        self.dfs(grid, x, y+1)
        self.dfs(grid, x-1, y)
        self.dfs(grid, x, y-1)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        curr_max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 1:
                    continue

                self.area = 0
                self.dfs(grid, i, j)
                curr_max_area = max(curr_max_area, self.area)

        return curr_max_area

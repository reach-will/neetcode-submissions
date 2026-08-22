class Solution:
    def dfs(self, grid: List[List[int]], x: int, y: int) -> int:
        if x < 0 or y < 0 or x >= self.ROWS or y >= self.COLS or grid[x][y] != 1:
            return 0

        grid[x][y] = 2

        return (1 + self.dfs(grid, x+1, y) +
                    self.dfs(grid, x, y+1) +
                    self.dfs(grid, x-1, y) +
                    self.dfs(grid, x, y-1)
                )

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])

        curr_max_area = 0

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if grid[i][j] != 1:
                    continue

                curr_max_area = max(curr_max_area, self.dfs(grid, i, j))

        return curr_max_area

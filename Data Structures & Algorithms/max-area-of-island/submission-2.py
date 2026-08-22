class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        x = len(grid[0])
        y = len(grid)
        
        largest_island = 0

        
        for i in range (y):
            for j in range(x): 
                if grid[i][j] == 1:
                    grid, size = self.sink_island(grid, i, j)
                    largest_island = max(size, largest_island)

        return largest_island


    def sink_island(self, grid, i, j)-> [List[List[int]], int]: 

        if grid[i][j] == 0: return [grid, 0]

        grid[i][j] = 0
        count = 1 
        if i - 1 > - 1:
            grid, add_ = self.sink_island(grid, i -1, j)  
            count  += add_
        if i + 1 < len(grid):
            grid, add_ = self.sink_island(grid, i + 1, j)  

            count  += add_
        if j - 1 > - 1:
            grid, add_ = self.sink_island(grid, i, j - 1)  
            count  += add_

        if j + 1 < len(grid[0]):
            grid, add_ = self.sink_island(grid, i, j + 1)  
            count  += add_
    
        return grid, count





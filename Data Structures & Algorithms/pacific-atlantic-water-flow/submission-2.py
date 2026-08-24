class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows, num_cols = len(heights), len(heights[0])
        pacific_rivers = set()
        atlantic_rivers = set()
        directions = ((1,0), (0,1), (-1,0), (0,-1))

        def dfs(row: int, col: int, river: set[tuple[int]]):
            river.add((row, col))
            for d_row, d_col in directions:
                nei_row, nei_col = row + d_row, col + d_col

                if not(0 <= nei_row < num_rows and 0 <= nei_col < num_cols) or (nei_row, nei_col) in river or heights[nei_row][nei_col] < heights[row][col]:
                    continue

                dfs(nei_row, nei_col, river)

        for i in range(num_rows):
            dfs(i, 0, pacific_rivers)
            dfs(i, num_cols - 1, atlantic_rivers)

        for j in range(num_cols):
            dfs(0, j, pacific_rivers)
            dfs(num_rows - 1, j, atlantic_rivers)

        return [e for e in pacific_rivers & atlantic_rivers]

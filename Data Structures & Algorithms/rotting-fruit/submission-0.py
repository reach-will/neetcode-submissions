class Solution:
    def valid_cell(self, row: int, col: int) -> bool:
        return 0 <= row < self.ROWS and 0 <= col < self.COLS

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        rot_source_queue = deque((row, col) for row in range(self.ROWS) for col in range(self.COLS) if grid[row][col] == 2)
        minute = 0

        while True:
            n = len(rot_source_queue)
            for _ in range(n):
                row, col = rot_source_queue.popleft()
                neighbor_cells = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]
                for nei_row, nei_col in neighbor_cells:
                    if not self.valid_cell(nei_row, nei_col) or grid[nei_row][nei_col] != 1:
                       continue

                    grid[nei_row][nei_col] = 2
                    rot_source_queue.append((nei_row, nei_col))

            if not rot_source_queue:
                break

            minute += 1

        if any(cell == 1 for row in grid for cell in row):
            return -1

        return minute
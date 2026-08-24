class Solution:
    def valid_cell(self, row: int, col: int, ROWS: int, COLS: int) -> bool:
        return 0 <= row < ROWS and 0 <= col < COLS

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rot_source_queue = deque()
        fresh = 0
        minute = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rot_source_queue.append((row, col))
                    continue
                if grid[row][col] == 1:
                    fresh += 1

        while fresh > 0 and rot_source_queue:
            n = len(rot_source_queue)
            for _ in range(n):
                row, col = rot_source_queue.popleft()
                neighbor_cells = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]
                for nei_row, nei_col in neighbor_cells:
                    if not self.valid_cell(nei_row, nei_col, ROWS, COLS) or grid[nei_row][nei_col] != 1:
                       continue

                    grid[nei_row][nei_col] = 2
                    fresh -= 1
                    rot_source_queue.append((nei_row, nei_col))

            minute += 1

        return minute if fresh == 0 else -1

class Solution:
    def valid_cell(self, row: int, col: int, ROWS: int, COLS: int) -> bool:
        return 0 <= row < ROWS and 0 <= col < COLS

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1,0),(0,1),(-1,0),(0,-1)]
        rot_source_queue = deque()
        fresh_count = 0
        minute = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rot_source_queue.append((row, col))

                elif grid[row][col] == 1:
                    fresh_count += 1

        while fresh_count > 0 and rot_source_queue:
            n = len(rot_source_queue)
            for _ in range(n):
                row, col = rot_source_queue.popleft()

                for d_row, d_col in DIRECTIONS:
                    if not self.valid_cell(row + d_row, col + d_col, ROWS, COLS) or grid[row + d_row][col + d_col] != 1:
                       continue

                    grid[row + d_row][col + d_col] = 2
                    fresh_count -= 1
                    rot_source_queue.append((row + d_row, col + d_col))

            minute += 1

        return minute if fresh_count == 0 else -1

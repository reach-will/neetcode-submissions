class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        rotten_queue = deque()
        fresh = 0
        minute = 0

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 2:
                    rotten_queue.append((row, col))

                elif grid[row][col] == 1:
                    fresh += 1

        while fresh > 0 and rotten_queue:
            for _ in range(len(rotten_queue)):
                row, col = rotten_queue.popleft()
                for d_row, d_col in directions:
                    nei_row, nei_col = row + d_row, col + d_col

                    if not (0 <= nei_row < num_rows and 0 <= nei_col < num_cols) or grid[nei_row][nei_col] != 1:
                       continue

                    grid[nei_row][nei_col] = 2
                    fresh -= 1
                    rotten_queue.append((nei_row, nei_col))

            minute += 1

        return minute if fresh == 0 else -1

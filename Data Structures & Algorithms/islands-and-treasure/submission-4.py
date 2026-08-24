class Solution:
    def valid(self, row: int, col: int) -> bool:
        return 0 <= row < self.ROWS and 0 <= col < self.COLS

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        INF = 2**31 - 1

        treasures = [(row, col) for row in range(self.ROWS)
                                for col in range(self.COLS)
                                if grid[row][col] == 0
                    ]
        treasure_queue = deque(treasures)

        depth = 1

        while treasure_queue:
            n = len(treasure_queue)
            for _ in range(n):
                row, col = treasure_queue.popleft()

                for nei_row, nei_col in [(row+1, col), (row, col+1), (row-1,col), (row,col-1)]:
                    if not self.valid(nei_row, nei_col) or grid[nei_row][nei_col] != INF:
                        continue

                    grid[nei_row][nei_col] = depth
                    treasure_queue.append((nei_row, nei_col))

            depth += 1

        return

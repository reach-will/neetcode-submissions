class Solution:
    def near_treasure(self, grid: List[List[int]], starting_row: int, starting_col: int) -> None:
        depth = 1
        cell_queue = deque([(starting_row + 1, starting_col), (starting_row, starting_col + 1), (starting_row - 1, starting_col), (starting_row, starting_col - 1)])

        while cell_queue:
            n = len(cell_queue)
            for _ in range(n):
                row, col = cell_queue.popleft()

                if row < 0 or col < 0 or row >= self.ROWS or col >= self.COLS or grid[row][col] <= depth:
                    continue

                grid[row][col] = depth
                cell_queue.extend([(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)])

            depth += 1

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.ROWS, self.COLS = len(grid), len(grid[0])

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if grid[row][col] != 0:
                    continue

                self.near_treasure(grid, row, col)

        return

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        num_rows, num_cols = len(board), len(board[0])
        directions = ((1,0), (0,1), (-1,0), (0,-1))
        safe_queue = deque()
        for row in range(num_rows):
            if board[row][0] == 'O':
                board[row][0] = 'S'
                safe_queue.append((row, 0))

            if board[row][num_cols - 1] == 'O':
                board[row][num_cols - 1] = 'S'
                safe_queue.append((row, num_cols - 1))

        for col in range(num_cols):
            if board[0][col] == 'O':
                board[0][col] = 'S'
                safe_queue.append((0, col))

            if board[num_rows - 1][col] == 'O':
                board[num_rows - 1][col] = 'S'
                safe_queue.append((num_rows - 1, col))

        while safe_queue:
            for _ in range(len(safe_queue)):
                row, col = safe_queue.popleft()
                for d_row, d_col in directions:
                    nei_row, nei_col = row + d_row, col + d_col

                    if not (0 <= nei_row < num_rows and 0 <= nei_col < num_cols) or board[nei_row][nei_col] != 'O':
                        continue

                    board[nei_row][nei_col] = 'S'
                    safe_queue.append((nei_row, nei_col))

        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'S':
                    board[row][col] = 'O'

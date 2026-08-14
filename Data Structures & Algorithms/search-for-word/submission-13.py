class Solution:
    def explore(self, x: int, y: int) -> bool:
        if self.depth == len(self.word):
            return True

        if x < 0 or x >= len(self.board) or y < 0 or y >= len(self.board[0]) or self.board[x][y] != self.word[self.depth] or self.board[x][y] == '#':
            return False

        self.board[x][y] = '#'
        self.depth += 1
        if self.explore(x+1, y) or self.explore(x, y+1) or self.explore(x-1, y) or self.explore(x, y-1):
            return True
        self.depth -= 1
        self.board[x][y] = self.word[self.depth]

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.depth = 0
        self.word = word
        self.board = board

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if self.explore(i, j):
                    return True

        return False

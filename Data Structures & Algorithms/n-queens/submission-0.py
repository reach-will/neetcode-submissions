class Solution:
    def backtrack(self, col: int) -> None:
        if len(self.path) == self.n:
            self.result.append(["." * i + "Q" + "." * (self.n - i - 1) for i in self.path])
            return
        for next_col in range(self.n):
            if not self.is_valid_path(next_col):
                continue
            self.path.append(next_col)
            self.backtrack(next_col)
            self.path.pop()
    def is_valid_path(self, col) -> bool:
        for q_i, q_j in enumerate(self.path):
            if q_j == col or q_j - q_i == col - len(self.path) or q_j + q_i == col + len(self.path):
                return False
        return True
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.path = []
        self.result = []
        self.backtrack(0)
        return self.result
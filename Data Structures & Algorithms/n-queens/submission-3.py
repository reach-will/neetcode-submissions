class Solution:
    def backtrack(self, col: int) -> None:
        if len(self.path) == self.n:
            self.result.append(["." * i + "Q" + "." * (self.n - i - 1) for i in self.path])
            return

        for next_col in range(self.n):
            if not self.is_valid_path(next_col):
                continue

            self.path.append(next_col)
            self.cols.add(next_col)
            self.diags.add(next_col - len(self.path))
            self.anti_diags.add(next_col + len(self.path))

            self.backtrack(next_col)

            self.anti_diags.remove(next_col + len(self.path))
            self.diags.remove(next_col - len(self.path))
            self.cols.remove(next_col)
            self.path.pop()

    def is_valid_path(self, col) -> bool:
        return not (col in self.cols or (col - len(self.path) - 1) in self.diags or (col + len(self.path) + 1) in self.anti_diags)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n

        self.path = []
        self.cols = set()
        self.diags = set()
        self.anti_diags = set()
        self.result = []
        self.backtrack(0)

        return self.result

class Solution:
    def backtrack(self) -> None:
        if len(self.path) == self.n:
            self.result.append(["." * i + "Q" + "." * (self.n - i - 1) for i in self.path])
            return

        for col in range(self.n):
            if not self.is_valid_path(len(self.path) + 1, col):
                continue

            self.path.append(col)

            self.cols.add(col)
            self.diags.add(len(self.path) - col)
            self.anti_diags.add(len(self.path) + col)

            self.backtrack()

            self.anti_diags.remove(len(self.path) + col)
            self.diags.remove(len(self.path) - col)
            self.cols.remove(col)

            self.path.pop()

    def is_valid_path(self, row, col) -> bool:
        return not (col in self.cols or (row - col) in self.diags or (row + col) in self.anti_diags)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n

        self.path = []
        self.cols = set()
        self.diags = set()
        self.anti_diags = set()
        self.result = []
        self.backtrack()

        return self.result

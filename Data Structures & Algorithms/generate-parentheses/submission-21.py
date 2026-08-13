class Solution:
    def backtrack(self, closed_n: int) -> None:
        if len(self.path) == 2 * self.n:
            self.result.append(''.join(self.path))
            return

        if len(self.path) - closed_n < self.n:
            self.path.append('(')
            self.backtrack(closed_n)
            self.path.pop()

        if len(self.path) > 2 * closed_n:
            self.path.append(')')
            self.backtrack(closed_n + 1)
            self.path.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.result = []
        self.path = []
        self.backtrack(0)
        return self.result

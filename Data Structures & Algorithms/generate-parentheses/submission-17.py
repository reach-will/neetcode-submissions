class Solution:
    def backtrack(self, open_n: int, closed_n: int) -> None:
        if len(self.path) == 2 * self.n:
            self.result.append(''.join(self.path))
            return

        if open_n < self.n:
            self.path.append('(')
            self.backtrack(open_n + 1, closed_n)
            self.path.pop()

        if open_n > closed_n:
            self.path.append(')')
            self.backtrack(open_n, closed_n + 1)
            self.path.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.result = []
        self.path = []
        self.backtrack(0, 0)
        return self.result

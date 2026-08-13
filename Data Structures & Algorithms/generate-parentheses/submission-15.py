class Solution:
    def backtrack(self, total: int) -> None:
        if len(self.path) == self.n:
            self.result.append("(".join([i * ")" for i in (self.path + [self.n - total])]))
            return

        for i in range(len(self.path) + 1 - total):
            self.path.append(i)
            self.backtrack(total + i)
            self.path.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.result = []
        self.path = []
        self.backtrack(0)
        return self.result

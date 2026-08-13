class Solution:
    def backtrack(self, start: int, remaining: int) -> None:
        if remaining == 0:
            self.result.append("(".join([i * ")" for i in self.path]))
            return
        if start > self.n:
            return
        for i in range(start + 1 - (self.n - remaining)):
            self.path.append(i)
            self.backtrack(start + 1, remaining - i)
            self.path.pop()
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.result = []
        self.path = []
        self.backtrack(0, n)
        return self.result
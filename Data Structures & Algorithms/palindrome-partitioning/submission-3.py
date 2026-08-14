class Solution:
    def backtrack(self, start: int) -> None:
        if start == self.n:
            self.result.append(self.path[:])
            return
        for end in range(start + 1, self.n + 1):
            if self.pal(start, end):
                self.path.append(self.s[start:end])
                self.backtrack(end)
                self.path.pop()
    def pal(self, i, j):              # is s[i:j] a palindrome?
        length = j - i
        return self.is_pal[length - 1][i]

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 1:
            return [[s]]
        is_pal = []
        is_pal.append([True] * n)
        is_pal.append([s[i] == s[i+1] for i in range(n - 1)])
        for step in range(2, n):
            # is_pal[step][i] => s[i:i + step + 1]
            # s[x:y] => is_pal[y - x - 1][y]
            # s[i + 1:i + step - 1] => is_pal[step - 2][i + 1]]
            is_pal.append([s[i] == s[i + step] and is_pal[step - 2][i + 1] for i in range(n - step)])

        self.s = s
        self.is_pal = is_pal
        self.n = n
        self.path = []
        self.result = []
        self.backtrack(0)

        return self.result
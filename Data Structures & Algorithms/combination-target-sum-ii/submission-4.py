class Solution:
    def backtrack(self, start: int, remaining: int) -> None:
        if remaining == 0:
            self.ans.append(self.path[:])
            return

        c = None
        for i in range(start, len(self.candidates)):
            if c == self.candidates[i]:
                continue

            c = self.candidates[i]
            if remaining < c:
                break

            self.path.append(c)
            self.backtrack(i + 1, remaining - c)
            self.path.pop()

        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()
        self.candidates = candidates
        self.path = []
        self.ans = []
        self.backtrack(0, target)
        return self.ans

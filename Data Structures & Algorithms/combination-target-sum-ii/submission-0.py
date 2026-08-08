class Solution:
    def backtrack(self, start: int, remaining: int) -> List[int]:
        if remaining == 0:
            return [[]]

        ans = []
        c = None
        for i in range(start, len(self.candidates)):
            if c == self.candidates[i]:
                continue

            c = self.candidates[i]
            if remaining < c:
                break

            ans += [[c] + e for e in self.backtrack(i + 1, remaining - c)]

        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()
        self.candidates = candidates
        return self.backtrack(0, target)

class Solution:
    def backtrack(self, start: int) -> None:
        if start == self.n:
            self.result.append("".join(self.path))
            return
        for ch in self.character_list(self.digits[start]):
            self.path.append(ch)
            self.backtrack(start + 1)
            self.path.pop()
    def character_list(self, digit: str) -> tuple[str]:
        return self.digit_character_set_map[int(digit) - 2]
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.digit_character_set_map = [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'), ('p', 'q', 'r', 's'), ('t', 'u', 'v'), ('w', 'x', 'y', 'z')]
        self.digits = digits
        self.n = len(digits)
        self.path = []
        self.result = []
        self.backtrack(0)
        return self.result
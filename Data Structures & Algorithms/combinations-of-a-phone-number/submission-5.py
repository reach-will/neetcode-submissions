class Solution:
    def backtrack(self, start: int) -> None:
        if start == self.n:
            self.result.append("".join(self.path))
            return

        for ch in self.digit_character_set_map[self.digits[start]]:
            self.path.append(ch)
            self.backtrack(start + 1)
            self.path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.digits = digits
        self.n = len(digits)

        self.digit_character_set_map = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }

        self.path = []
        self.result = []
        self.backtrack(0)

        return self.result
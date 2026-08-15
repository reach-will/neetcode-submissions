class Solution:
    def backtrack(self, start: int) -> None:
        if start == self.n:
            self.result.append(''.join(self.path))
            return

        for ch in self.digit_to_characters[self.digits[start]]:
            self.path.append(ch)
            self.backtrack(start + 1)
            self.path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.digits = digits
        self.n = len(digits)

        self.digit_to_characters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        self.path = []
        self.result = []
        self.backtrack(0)

        return self.result

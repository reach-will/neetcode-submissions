class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = Counter()
        j = max_f = 0
        for i, ch in enumerate(s):
            c[ch] += 1
            max_f = max(max_f, c[ch])
            if max_f < i - j + 1 - k:
                c[s[j]] -= 1
                j += 1
        return i - j + 1
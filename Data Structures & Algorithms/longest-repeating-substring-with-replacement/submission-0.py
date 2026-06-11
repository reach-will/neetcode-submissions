class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = Counter()
        i = j = 0
        for i, ch in enumerate(s):
            c[ch] += 1
            if max(c.values()) <= i - j - k:
                c[s[j]] -= 1
                j += 1
        return i - j + 1
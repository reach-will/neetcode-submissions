class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = Counter()
        j = maxf = 0
        for i, ch in enumerate(s):
            c[ch] += 1
            maxf = max(maxf, c[ch])
            if maxf < i - j + 1 - k:
                c[s[j]] -= 1
                j += 1
        return i - j + 1
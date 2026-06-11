class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        j = 0
        c = Counter()
        for i, ch in enumerate(s):
            c[ch] += 1
            if len(c.keys()) <= i - j:
                if c[s[j]] > 1:
                    c[s[j]] -= 1
                else:
                    del c[s[j]]
                j += 1
        return i - j + 1
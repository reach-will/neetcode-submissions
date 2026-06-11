class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = max_len = 0
        m = {}
        for i, ch in enumerate(s):
            if m.get(s[i], -1) >= j:
                j = m[s[i]] + 1
            m[ch] = i
            max_len = max(max_len, i - j + 1)
        return max_len
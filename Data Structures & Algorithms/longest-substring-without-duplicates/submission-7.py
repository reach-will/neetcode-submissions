class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        j = max_len = 0
        m = {}
        for i, ch in enumerate(s):
            if s[i] in m and m[s[i]] >= j:
                j = m[s[i]] + 1
            m[ch] = i
            max_len = max(max_len, i - j + 1)
        return max_len
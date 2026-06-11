class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        c = Counter(t)
        missing = len(c)
        i = 0
        for i, ch in enumerate(s):
            c[ch] -= 1
            if ch in c and c[ch] == 0:
                missing -= 1
                if missing == 0:
                    break
        if missing != 0:
            return ""
        j = 0
        while c[s[j]] < 0:
            c[s[j]] += 1
            j += 1
        ans_i, ans_j = i, j
        for i, ch in enumerate(s[i + 1:], start = i + 1):
            c[ch] -= 1
            while c[s[j]] < 0:
                c[s[j]] += 1
                j += 1
            if i - j < ans_i - ans_j:
                ans_i, ans_j = i, j
        return s[ans_j:ans_i + 1]
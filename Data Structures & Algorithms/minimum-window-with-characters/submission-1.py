class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        ans = ""
        c = Counter(t)
        t_keys = iter(list(c.keys()))
        i = j = 0
        curr_key = next(t_keys)
        for i, ch in enumerate(s):
            c[ch] -= 1
            while c[curr_key] <= 0:
                curr_key = next(t_keys, None)
                if not curr_key:
                    while c[s[j]] < 0:
                        c[s[j]] += 1
                        j += 1
                    ans = s[j:i + 1]
                    break
            if not curr_key:
                break
        if curr_key:
            return ans
        for i, ch in enumerate(s[i + 1:], start = i + 1):
            c[ch] -= 1
            while c[s[j]] < 0:
                c[s[j]] += 1
                j += 1
            if i - j + 1 < len(ans):
                ans = s[j:i + 1]
        return ans
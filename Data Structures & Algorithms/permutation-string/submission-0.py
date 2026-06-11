class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permut = Counter(s1)
        j = 0
        c = Counter()
        for i, ch in enumerate(s2):
            c[ch] += 1
            while permut[ch] < c[ch]:
                c[s2[j]] -= 1
                j += 1
            if i - j + 1 == len(s1):
                return True
        return False
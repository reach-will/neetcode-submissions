from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lens, lent = len(s), len(t)
        if len(s) != len(t):
            return False
        occurences_dict_s = defaultdict(int)
        occurences_dict_t = defaultdict(int)
        for i in range(lens):
            occurences_dict_s[s[i]] += 1
            occurences_dict_t[t[i]] += 1
        return occurences_dict_s == occurences_dict_t
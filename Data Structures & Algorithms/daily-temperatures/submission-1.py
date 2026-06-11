class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        unsolved = []

        for i in range(len(temperatures)):
            cur = temperatures[i]

            while unsolved and unsolved[-1][0] < cur:
                temp, j = unsolved.pop()
                res[j] = i - j
            
            unsolved.append([cur, i])
        
        return res
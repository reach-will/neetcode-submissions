class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 1:
            return [[s]]
        is_pal = []
        is_pal.append([True] * n)
        is_pal.append([s[i] == s[i+1] for i in range(n - 1)])
        for step in range(2, n):
            # is_pal[step][i] => s[i:i + step + 1]
            # s[x:y] => is_pal[y - x - 1][y]
            # s[i + 1:i + step - 1] => is_pal[step - 2][i + 1]]
            is_pal.append([s[i] == s[i + step] and is_pal[step - 2][i + 1] for i in range(n - step)])

        def pal(i, j):              # is s[i:j] a palindrome?
            length = j - i
            return is_pal[length - 1][i]

        # solutions[j] = all palindrome partitions of s[0:j]
        solutions = [[[]]]   # solutions[0] = one partition: the empty one
        for j in range(1, n + 1):
            combined = []
            for i in range(j):
                if pal(i, j):
                    last_piece = s[i:j]
                    for left in solutions[i]:
                        combined.append(left + [last_piece])
            solutions.append(combined)

        return solutions[-1]
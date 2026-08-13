class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(open, closed, current):
            if len(current) == 2 * n:
                output.append(''.join(current))
                return
            if open < n:
                current.append('(')
                backtrack(open + 1, closed, current)
                current.pop()
            if open > closed:
                current.append(')')
                backtrack(open, closed + 1, current)
                current.pop()

        backtrack(0, 0, [])
        return output

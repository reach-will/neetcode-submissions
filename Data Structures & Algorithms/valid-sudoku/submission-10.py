class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue
                if cell in rows[i]:
                    return False
                rows[i].add(cell)
                if cell in cols[j]:
                    return False
                cols[j].add(cell)
                if cell in squares[(i // 3) * 3 + j // 3]:
                    return False
                squares[(i // 3) * 3 + j // 3].add(cell)
        return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sets = [set() for _ in range(27)]
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue
                if cell in sets[i]:
                    return False
                sets[i].add(cell)
                if cell in sets[9 + j]:
                    return False
                sets[9 + j].add(cell)
                if cell in sets[18 + (i // 3) * 3 + j // 3]:
                    return False
                sets[18 + (i // 3) * 3 + j // 3].add(cell)
        return True
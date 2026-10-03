class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sections = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                row = i
                col = j
                sec = (i//3) +((j//3) *3)
                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[row] or num in cols[col] or num in sections[sec]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                sections[sec].add(num)
        return True
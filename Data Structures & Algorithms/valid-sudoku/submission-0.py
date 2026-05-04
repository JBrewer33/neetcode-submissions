class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        quad = [set() for _ in range(9)]

        for i in range(9):
            
            for j in range(9):
                key = board[i][j]
                if key == ".":
                    continue
                q = ((i // 3) * 3 + (j // 3))
                print(q)
                if key in row[i] or key in col[j] or key in quad[q]:
                    return False
                row[i].add(key)
                col[j].add(key)
                quad[q].add(key)
        return True

                

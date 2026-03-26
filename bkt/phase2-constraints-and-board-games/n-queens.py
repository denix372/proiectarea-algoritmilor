from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]
        
        def back(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return


            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c) 
                board[r][c] = 'Q'

                back(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c) 
                board[r][c] = '.'

        back(0)
        return res

sol = Solution()

for board in sol.solveNQueens(4):
    for r in board:
        for c in r:
            print(c + " ", end = "")
        print()
    print()
class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()

        cnt = [0]
        res = []
        board = [["."] * n for i in range(n)]
        
        def back(r):
            if r == n:
                cnt[0] += 1
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
        return cnt[0]
    
sol = Solution()
print(sol.totalNQueens(8))
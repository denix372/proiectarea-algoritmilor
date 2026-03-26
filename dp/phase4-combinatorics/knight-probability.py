from typing import List
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,1),(1,2),(-1,2),(-2,1),
                 (-2,-1),(-1,-2),(1,-2),(2,-1)]

        dp = [[[0]*n for _ in range(n)] for _ in range(k+1)]
        dp[0][row][column] = 1

        for step in range(1, k+1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            dp[step][nr][nc] += dp[step-1][r][c] / 8
        
        return sum(dp[k][r][c] for r in range(n) for c in range(n))

sol = Solution()
n = 3
k = 2
row = 0
column = 0
print(sol.knightProbability(n, k, row, column))
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[1][1] = grid[0][0]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i ==1 and j == 1:
                    continue
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]
        
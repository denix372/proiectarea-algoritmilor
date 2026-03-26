from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf')] * (n + 2) for i in range(n)]

        for j in range(1, n + 1):
            dp[0][j] = matrix[0][j - 1]

        for i in range(1, n):
            for j in range(1, n + 1):
                dp[i][j] = matrix[i][j - 1] + min(dp[i - 1][j - 1], 
                                                    dp[i - 1][j],
                                                    dp[i - 1][j + 1])
        best = dp[n - 1][1]
        for j in range(1, n + 1):
            best = min(best, dp[n - 1][j])
        return best
        
matrix = [[2,1,3],[6,5,4],[7,8,9]]
sol = Solution()
print(sol.minFallingPathSum(matrix))
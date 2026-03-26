from typing import List
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):  # triangle must have at least 3 vertices
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][n - 1]

values = [1,3,1,4,1,5]
print(Solution().minScoreTriangulation(values))
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[1][1] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if not (i == 1 and j == 1):
                    if obstacleGrid[i - 1][j - 1] != 1:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n][m]
    
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
sol = Solution()
print(sol.uniquePathsWithObstacles(obstacleGrid))
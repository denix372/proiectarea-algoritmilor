from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        cnt = 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j], 
                                       dp[i][j - 1], 
                                       dp[i - 1][j - 1])
                    cnt += dp[i][j]

        return cnt

sol = Solution()
matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
print(sol.countSquares(matrix))
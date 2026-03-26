from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        best = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] != "0":
                    dp[i][j] = 1 + min(dp[i - 1][j], 
                                       dp[i][j - 1],
                                        dp[i - 1][j - 1])
                best = max(best, dp[i][j])
        return best * best
        
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
sol = Solution()
print(sol.maximalSquare(matrix))
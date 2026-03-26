from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(length + 1)]

        for i in range(1, length + 1):
            ones = strs[i - 1].count("1")
            zeros = strs[i - 1].count("0")

            for j in range( n + 1):
                for k in range( m + 1):
                    if j>= ones and k >= zeros:
                        dp[i][j][k] = max(dp[i - 1][j][k], 
                            dp[i - 1][j - ones][k - zeros] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        return dp[length][n][m]
    
class Solution2:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, length + 1):
            ones = strs[i - 1].count("1")
            zeros = strs[i - 1].count("0")

            for j in range(n, ones - 1, -1):
                for k in range(m, zeros - 1, -1):
                    dp[j][k] = max(dp[j][k], 
                            dp[j - ones][k - zeros] + 1)
        return dp[n][m]
        
        

sol = Solution2()
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
print(sol.findMaxForm(strs, m, n))
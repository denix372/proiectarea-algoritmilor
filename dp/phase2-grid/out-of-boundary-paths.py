MOD = 10**9 + 7
class Solution:
    def findPaths(self, n: int, m: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0] * (maxMove + 1) for _ in range (m + 2)] for _ in range(n + 2)]
        dp[startRow + 1][startColumn + 1][0] = 1

        for k in range(1, maxMove + 1):
            for i in range(1, n + 1):
                for j in range(1, m + 1):

                    for di, dj in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                        ni = i + di
                        nj = j + dj
                        dp[ni][nj][k] += dp[i][j][k - 1] % MOD
        res = 0
        for k in range(1, maxMove + 1):
            for i in range(1, n + 1):
                res = (res + dp[i][0][k] + dp[i][m + 1][k]) % MOD
                
            for j in range(1, m + 1):
                res = (res + dp[0][j][k] + dp[n + 1][j][k]) % MOD

        return res % MOD

m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1
print(Solution().findPaths(m, n, maxMove, startRow, startColumn))
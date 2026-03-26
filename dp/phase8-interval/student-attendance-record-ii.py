from typing import List
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for a in range(2):
                for l in range(3):
                    val = dp[i-1][a][l]
                    if val == 0:
                        continue

                    dp[i][a][0] = (dp[i][a][0] + val) % MOD

                    if l < 2:
                        dp[i][a][l+1] = (dp[i][a][l+1] + val) % MOD

                    if a == 0:
                        dp[i][1][0] = (dp[i][1][0] + val) % MOD

        ans = 0
        for a in range(2):
            for l in range(3):
                ans = (ans + dp[n][a][l]) % MOD

        return ans
    

sol = Solution()
n = 10101
print(sol.checkRecord(n))
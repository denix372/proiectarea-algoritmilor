MOD = 10**9 + 7
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        dp[0][0] = 1  # 0 dices => target = 0 in 1 way

        for d in range(1, n + 1):
            for s in range(1, target + 1):
                for face in range(1, k + 1):
                    if s - face >= 0:
                        dp[d][s] = (dp[d][s] + dp[d - 1][s - face]) % MOD

        return dp[n][target]
    

n = 30
k = 30
target = 500
sol = Solution()
print(sol.numRollsToTarget(n, k, target))
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        return dp[n] - 1

n = 3
print(Solution().minSteps(n))
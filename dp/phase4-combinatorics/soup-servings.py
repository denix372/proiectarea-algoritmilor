class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0
        n = (n + 24) // 25
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]

        for a in range(n + 1):
            for b in range(n + 1):
                if a == 0 and b == 0:
                    dp[a][b] = 0.5
                elif a == 0:
                    dp[a][b] = 1.0
                elif b == 0:
                    dp[a][b] = 0.0
                else:
                    dp[a][b] = 0.25 * (
                        dp[max(0, a - 4)][b] +
                        dp[max(0, a - 3)][max(0, b - 1)] +
                        dp[max(0, a - 2)][max(0, b - 2)] +
                        dp[max(0, a - 1)][max(0, b - 3)]
                    )
        
        return dp[n][n]

n = 50
print(Solution().soupServings(n))
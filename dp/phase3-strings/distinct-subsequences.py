class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(0, n + 1):
            dp[i][0] = 1  # best case, t is empty

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    # use this matching character -> dp[i-1][j-1]
                    # OR skip this character in s -> dp[i - 1][j]
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    # if it doesn't match, we only skip the character from s
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]


s = "rabbbit"
t = "rabbit"
print(Solution().numDistinct(s, t))
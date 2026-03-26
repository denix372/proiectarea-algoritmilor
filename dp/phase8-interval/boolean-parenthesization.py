class Solution:
    def countWays(self, s):
        n = len(s)

        true_dp = [[0] * n for _ in range(n)]
        false_dp = [[0] * n for _ in range(n)]

        for i in range(0, n, 2):
            if s[i] == 'T':
                true_dp[i][i] = 1
            else:
                false_dp[i][i] = 1

        # Fill DP for lengths 3, 5, 7, ...
        for length in range(3, n + 1, 2):
            for i in range(0, n - length + 1, 2):
                j = i + length - 1

                for k in range(i + 1, j, 2):
                    lt = true_dp[i][k - 1]
                    lf = false_dp[i][k - 1]
                    rt = true_dp[k + 1][j]
                    rf = false_dp[k + 1][j]

                    if s[k] == '&':
                        true_dp[i][j] += lt * rt
                        false_dp[i][j] += lt * rf + lf * rt + lf * rf

                    elif s[k] == '|':
                        true_dp[i][j] += lt * rt + lt * rf + lf * rt
                        false_dp[i][j] += lf * rf

                    elif s[k] == '^':
                        true_dp[i][j] += lt * rf + lf * rt
                        false_dp[i][j] += lt * rt + lf * rf

        return true_dp[0][n - 1]
    

sol = Solution()
s = "T|T&F^T"
print(sol.countWays(s))
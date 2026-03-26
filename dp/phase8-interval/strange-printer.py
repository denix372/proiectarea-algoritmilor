from typing import List

class Solution:
    def strangePrinter(self, s: str) -> int:
        # OPTIONAL TRICK: Compress consecutive duplicates (e.g. "aaabbb" -> "ab")
        # because "aaa" takes the exact same number of turns as "a".
        # This speeds up the DP immensely!
        s = "".join(a for a, b in zip(s, s[1:] + "-") if a != b)
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = float('inf')
                    # They don't match, so we try splitting the string at every k
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
    
        return dp[0][n - 1]

s = "aaabbb"
print(Solution().strangePrinter(s))
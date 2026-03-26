from typing import List

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [[0] * n for _ in range(n)]

        def sum(i, j):
            s = 0
            for k in range(i, j):
                s += stones[k]
            return s

        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                dp[i][j] = max(get_sum(i + 1, j) - dp[i + 1][j],
                                get_sum(i, j - 1) - dp[i][j - 1])

        return dp[0][n - 1]

stones = [5,3,1,4,2]
print(Solution().stoneGameVII(stones))
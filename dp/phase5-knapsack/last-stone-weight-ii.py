from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        s = total // 2

        dp = [[False] * (s + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if j < stones[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i - 1]]
        
        for j in range(s, -1, -1):
            if dp[n][j]:
                return total - 2 * j

stones = [31,26,33,21,40]
print(Solution().lastStoneWeightII(stones))
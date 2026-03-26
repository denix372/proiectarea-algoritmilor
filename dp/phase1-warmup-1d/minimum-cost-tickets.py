from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (days[n - 1] + 1)
        travel = set(days)

        for i in range(1, days[n - 1] + 1):
            if i not in travel:
                dp[i] = dp[i - 1]
                continue

            dp[i] = costs[0] + dp[i - 1]
            if i >= 7:
                dp[i] = min(dp[i], costs[1] + dp[i - 7])
            else:
                dp[i] = min(dp[i], costs[1] + dp[0])
            if i >= 30:
                dp[i] = min(dp[i], costs[2] + dp[i - 30])
            else:
                dp[i] = min(dp[i], costs[2] + dp[0])

        return dp[days[n - 1]]


sol = Solution()
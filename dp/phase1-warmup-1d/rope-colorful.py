from typing import List
INF = 10**18
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        def code(c):
            return ord(c) - ord('a') + 1

        dp = [[INF] * 27 for _ in range(n)]
        groupMax = [0] * n

        firstColor = code(colors[0])
        dp[0][firstColor] = 0
        groupMax[0] = neededTime[0]

        for i in range(1, n):
            curr = code(colors[i])
            t = neededTime[i]

            dp[i][curr] = dp[i-1][curr] + min(t, groupMax[i-1])
            groupMax[i] = max(groupMax[i-1], t)

            best_prev = min(dp[i-1][c] for c in range(27) if c != curr)
            dp[i][curr] = min(dp[i][curr], best_prev)
            if best_prev < dp[i-1][curr]:
                groupMax[i] = t

        return min(dp[n-1])

                
colors = "aabaa"
neededTime = [1,2,3,4,1]
sol = Solution()
print(sol.minCost(colors, neededTime))
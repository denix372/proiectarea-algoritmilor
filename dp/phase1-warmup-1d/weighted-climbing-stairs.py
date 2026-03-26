class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        dp[n - 1] = cost[n - 1]
        dp[n - 2] = cost[n - 2]
        
        for i in range(n - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(Solution().minCostClimbingStairs(cost))
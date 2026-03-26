from typing import List

# Similar to Unbounded knapsack
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[amount + 1] * (amount + 1) for _ in range(n)]
    
        for i in range(n):
            dp[i][0] = 0
        for i in range(n):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i]] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]
        if dp[n - 1][amount] != amount + 1:
            return dp[n - 1][amount]
        return -1
    
# Regular solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(n):
            for j in range(coins[i], amount + 1):
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        if dp[amount] != amount + 1:
            return dp[amount]
        return -1
        

sol = Solution()
coins = [1,2,5]
amount = 11
print(sol.coinChange(coins, amount))
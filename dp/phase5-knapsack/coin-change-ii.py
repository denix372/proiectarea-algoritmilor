from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        # the order doesn't matter
        for i in range(n):
            for j in range(coins[i], amount + 1):
                dp[j] +=  dp[j - coins[i]]

        return dp[amount]
        

sol = Solution()
amount = 5
coins = [1,2,5]
print(sol.change(amount, coins))
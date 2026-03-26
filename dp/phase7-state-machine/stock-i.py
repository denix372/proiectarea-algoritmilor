from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = [0] * n
        sell = [0] * n

        buy[0] = prices[0]
        sell[0] = 0
        for i in range(1, n):
            buy[i] = min(buy[i - 1], prices[i])
            sell[i] = max(sell[i - 1], prices[i] - buy[i - 1])
        return sell[n - 1]
        

sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))
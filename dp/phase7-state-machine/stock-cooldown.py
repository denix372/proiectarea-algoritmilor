from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        buy = [0] * n
        sell = [0] * n

        buy[0] = prices[0]
        sell[0] = 0
        buy[1] = min(buy[0], prices[1])
        sell[1] = max(sell[0], prices[1] - buy[0])
        for i in range(2, n):
            buy[i] = min(buy[i - 1], prices[i] - sell[i - 2])
            sell[i] = max(sell[i - 1], prices[i] - buy[i - 1])
        return sell[n - 1]

prices = [1,2,3,0,2]
print(Solution().maxProfit(prices))
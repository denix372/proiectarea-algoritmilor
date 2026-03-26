from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = [0] * n
        sell = [0] * n

        buy[0] = prices[0]
        sell[0] = 0
        for i in range(1, n):
            buy[i] = min(buy[i - 1], prices[i] - sell[i - 1])
            sell[i] = max(sell[i - 1], prices[i] - buy[i - 1] - fee)
        return sell[n - 1]

prices = [1,3,2,8,4,9]
fee = 2
print(Solution().maxProfit(prices, fee))
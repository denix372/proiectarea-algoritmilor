from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = [0] * n
        sell1 = [0] * n
        buy2 = [0] * n
        sell2 = [0] * n

        buy1[0] = prices[0]
        buy2[0] = prices[0]
        sell1[0] = 0
        sell2[0] = 0
        for i in range(1, n):
            buy1[i] = min(buy1[i - 1], prices[i])
            sell1[i] = max(sell1[i - 1], prices[i] - buy1[i - 1])
            buy2[i] = min(buy2[i - 1], prices[i] - sell1[i - 1])
            sell2[i] = max(sell2[i - 1], prices[i] - buy2[i - 1])
        return sell2[n - 1]

prices = [3,3,5,0,0,3,1,4]
print(Solution().maxProfit(prices))
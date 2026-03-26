from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        buy = [[0] * n for _ in range(k)]
        sell = [[0] * n for _ in range(k)]

        for j in range(k):
            buy[j][0] = prices[0]
            sell[j][0] = 0

        for j in range(k):
            for i in range(1, n):
                if j == 0:
                    buy[j][i] = min(buy[j][i - 1], prices[i])
                    sell[j][i] = max(sell[j][i - 1], prices[i] - buy[j][i - 1])
                    continue

                buy[j][i] = min(buy[j][i - 1], prices[i] - sell[j - 1][i - 1])
                sell[j][i] = max(sell[j][i - 1], prices[i] - buy[j][i - 1])
        return sell[k - 1][n - 1]

k = 2
prices = [2,4,1]
print(Solution().maxProfit(k, prices))
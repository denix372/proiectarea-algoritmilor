from typing import List

class Solution:
    def final_prices(self, prices: List[int]) -> List[int]:
        res = prices.copy()
        stack = []

        for i, v in enumerate(prices):
            while stack and v <= stack[-1][1]:
                j, w = stack.pop()
                res[j] = w - v
            stack.append((i, v))

        return res

prices = [8,4,6,2,3]
print(Solution().finalPrices(prices))
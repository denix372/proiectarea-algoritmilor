from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)

        for c in costs:
            freq[c] += 1
        bars = 0

        for cost in range(1, max_cost + 1):
            if freq[cost] == 0:
                continue
            can_buy = min(freq[cost], coins // cost)
            bars += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break
        return bars
costs = [1,3,2,4,1]
coins = 7
print(Solution().maxIceCream(costs, coins))
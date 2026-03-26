from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            for k in dp[stone]:
                for step in (k - 1, k, k + 1):
                    if step > 0 and (stone + step) in dp:
                        dp[stone + step].add(step)

        last_stone = stones[-1]
        return len(dp[last_stone]) > 0

stones = [0,1,3,5,6,8,12,17]
print(Solution().canCross(stones))
from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2

            res = 0
            for p in piles:
                res += ceil(p/k)

            if res <= h:
                right = k - 1
            else:
                left = k + 1
        return left

        
piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))
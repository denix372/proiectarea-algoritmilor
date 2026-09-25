from typing import List
from heapq import heappush, heappop

class Solution:
    def last_stone_weight(self, stones: List[int]) -> int:
        q = []
        for x in stones:
            heappush(q, - x)
        
        while len(q) > 1:
            x, y = heappop(q), heappop(q)
            heappush(q, min(x, y) - max(x, y))
        
        if q:
            return - heappop(q)
        return 0

stones = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones))
from typing import List
from heapq import heappush, heappop

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        q = []

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                if len(q) < ladders:
                    heappush(q, diff)
                else:
                    if not q or q[0] >= diff:
                        bricks -= diff
                    else:
                        poll = heappop(q)
                        heappush(q, diff)
                        bricks -= poll
                    if bricks < 0:
                        return i
        return n - 1

heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
print(Solution().furthestBuilding(heights, bricks, ladders))
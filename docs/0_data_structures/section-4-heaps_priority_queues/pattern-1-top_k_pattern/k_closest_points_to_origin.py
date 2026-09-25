from typing import List
from heapq import heappush, heappop

class Solution:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x * x + y * y

        q = []
        for x, y in points:
            heappush(q, (dist(x, y), x, y))
        
        res = []
        for _ in range(k):
            _, x, y = heappop(q)
            res.append([x, y])
        
        return res

points = [[1,3],[-2,2]]
k = 1
print(Solution().kClosest(points, k))
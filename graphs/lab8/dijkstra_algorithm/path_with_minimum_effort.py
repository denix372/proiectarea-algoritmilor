from typing import List
from heapq import heappush, heappop
INF = 10 **6
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = 0
        q = []
        heappush(q, (0, (0, 0)))

        while q:
            d, (x, y) = heappop(q)
            if d > dist[x][y]:
                continue
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    w = max(dist[x][y], abs(heights[x][y] - heights[nx][ny]))
                    if w < dist[nx][ny]:
                        dist[nx][ny] = w
                        heappush(q, (dist[nx][ny], (nx, ny)))
        return dist[n - 1][m - 1]
        
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(Solution().minimumEffortPath(heights))
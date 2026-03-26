from typing import List
from heapq import heappush, heappop
INF = 10**9

INF = 10**9
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[INF] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        q = []
        heappush(q, (grid[0][0], (0, 0)))
        while q:
            d, (x, y) = heappop(q)

            if d > dist[x][y]:
                continue

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    if max(dist[x][y], grid[nx][ny]) < dist[nx][ny]:
                        dist[nx][ny] = max(dist[x][y], grid[nx][ny]) 
                        heappush(q, (dist[nx][ny], (nx, ny)))
        return dist[n - 1][n - 1]

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
sol = Solution()
print(sol.swimInWater(grid))
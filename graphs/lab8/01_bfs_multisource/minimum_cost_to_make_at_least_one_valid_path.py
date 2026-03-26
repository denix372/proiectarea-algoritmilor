from typing import List
from collections import deque
INF = 10**9

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()

        dist = [[INF] * m for _ in range(n)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q.append((0, 0))
        dist[0][0] = 0

        while q:
            x, y = q.popleft()

            for d, (dx, dy) in enumerate(dirs, start=1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:

                    cost = 0 if grid[x][y] == d else 1
                    new_cost = dist[x][y] + cost

                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        if cost == 0:
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))

        return dist[n - 1][m - 1]

grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
print(Solution().minCost(grid))
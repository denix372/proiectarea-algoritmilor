from typing import List
from collections import deque

INF = 10**5 + 1

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = grid[0][0]
        q = deque([(grid[0][0], (0, 0))])

        while q:
            d, (i, j) = q.popleft()

            if d > dist[i][j]:
                continue
    
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == INF:
                    if grid[ni][nj] == 0:
                        dist[ni][nj] = dist[i][j]
                        q.appendleft((dist[ni][nj], (ni, nj)))
                    else:
                        dist[ni][nj] = dist[i][j] + grid[ni][nj]
                        q.append((dist[ni][nj], (ni, nj)))

        return dist[n - 1][m - 1]

grid = [[0,1,1],[1,1,0],[1,1,0]]
print(Solution().minimumObstacles(grid))
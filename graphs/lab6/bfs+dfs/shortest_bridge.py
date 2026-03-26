from typing import List
from collections import deque
INF = 10**6
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        first = [[False] * m for _ in range(n)]

        def dfs(x, y):
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx = dx + x
                ny = dy + y

                if 0 <= nx < n and 0 <= ny < m:
                    if first[nx][ny] == False and grid[nx][ny] == 1:
                        first[nx][ny] = True 
                        dfs(nx, ny)

        for i in range(n):
            ok = 0
            for j in range(m):
                if grid[i][j] == 1:
                    #first island
                    first[i][j] = True
                    dfs(i, j)
                    ok = 1
                    break
            if ok == 1:
                break

        q = deque()
        visited = [[False] * m for _ in range(n)]
        dist = [[INF] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if first[i][j]:
                    q.append((i, j))
                    dist[i][j] = 0
                    visited[i][j] = True

        while q:
            x, y = q.popleft()

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx = dx + x
                ny = dy + y

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == False:
                        
                        if grid[nx][ny] == 1 and first[nx][ny] == False:
                            return dist[x][y]

                        dist[nx][ny] = dist[x][y] + 1
                        visited[nx][ny] = True
                        q.append((nx, ny))
        return 0
    
sol = Solution()
grid = [[0,1,0],[0,0,0],[0,0,1]]
print(sol.shortestBridge(grid))
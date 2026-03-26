from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        pac = [[False] * m for _ in range(n)]
        atl = [[False] * m for _ in range(n)]
        
        def dfs(x, y, visited):
            visited[x][y] = True
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny, visited)
        for i in range(n):
            dfs(i, 0, pac)
        for j in range(m):
            dfs(0, j, pac)

        for i in range(n):
            dfs(i, m - 1, atl)
        for j in range(m):
            dfs(n - 1, j, atl)
        res = []
        for i in range(n):
            for j in range(m):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        return res
            
sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(sol.pacificAtlantic(heights))
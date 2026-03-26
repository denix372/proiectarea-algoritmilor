from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _  in range(n)]

        def dfs(x, y):
            if x >= n or y >= m or x < 0 or y < 0:
                return 1
            if grid[x][y] == 0:
                return 1
            if visited[x][y]:
                return 0

            visited[x][y] = True
            t = 0
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                t += dfs(x + dx, y + dy)
            return t
    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i, j)    
        return 0
    
sol = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(sol.islandPerimeter(grid))
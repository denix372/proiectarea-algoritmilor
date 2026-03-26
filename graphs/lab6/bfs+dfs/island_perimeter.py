from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 1
            
            if grid[i][j] == 0:
                return 1

            if visited[i][j]:
                return 0

            visited[i][j] = True

            perim = 0
            perim += dfs(i - 1, j)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i, j + 1)
            return perim

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0
    
sol = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(sol.islandPerimeter(grid))
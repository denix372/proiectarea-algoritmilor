from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        visited = [[False] * m for _ in range(n)]

        def dfs(x, y):
            visited[x][y] = True

            for dx, dy in [(0,1), (1, 0), (-1, 0), (0, -1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and grid[nx][ny] == '1':
                        dfs(nx, ny)
            
        nr = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == '1':
                    nr += 1
                    dfs(i, j)
        return nr
        
sol = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid))
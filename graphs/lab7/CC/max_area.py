from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        visited = [[False] * m for _ in range(n)]

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0 or visited[x][y]:
                    return 0
            visited[x][y] = True
            return 1 + dfs(x + 1, y) +  dfs(x - 1, y) +  dfs(x, y + 1) +  dfs(x, y - 1)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    res = max(res, dfs(i, j))
        return res
        
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))
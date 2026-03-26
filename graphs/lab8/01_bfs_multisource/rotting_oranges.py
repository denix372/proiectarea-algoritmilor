from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        q = deque()
        fresh_count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_count += 1
                    
        res = 0
        while q:
            i, j, d = q.popleft()
            res = d

            for di, dj in dirs:
                ni, nj = i + di, j + dj

                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh_count -= 1
                    q.append((ni, nj, d + 1))

        return res if fresh_count == 0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))
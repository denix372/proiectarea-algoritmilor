class Solution:
    def uniquePathsIII(self, grid):
        m, n = len(grid), len(grid[0])
        empty = 0
        sx = sy = 0

        # find start and count empty squares
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                if grid[i][j] != -1:
                    empty += 1

        def back(x, y, cnt):
            if grid[x][y] == 2:
                return 1 if cnt == empty else 0

            temp = grid[x][y]
            grid[x][y] = -1  # mark as visited 

            paths = 0
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    paths += back(nx, ny, cnt + 1)

            grid[x][y] = temp  # backtrack
            return paths

        return back(sx, sy, 1)


sol = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
print(sol.uniquePathsIII(grid))
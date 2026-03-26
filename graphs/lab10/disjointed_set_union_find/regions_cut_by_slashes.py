
class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        parent = [i for i in range(4 * n * n)]
        cnt = 4 * n * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            nonlocal cnt
            rx = find(x)
            ry = find(y)

            if rx != ry:
                parent[rx] = ry
                cnt -= 1
        
        for i in range(n):
            for j in range(n):
                base = 4 * (i * n + j)
                val = grid[i][j]
                
                if val == '/':
                    union(base + 0, base + 3)
                    union(base + 1, base + 2)
                elif val == '\\':
                    union(base + 0, base + 1)
                    union(base + 2, base + 3)
                else:
                    union(base + 0, base + 1)
                    union(base + 1, base + 2)
                    union(base + 2, base + 3)
                
                if j + 1 < n:
                    base_right = 4 * (i * n + (j + 1))
                    union(base + 1, base_right + 3)
                
                if i + 1 < n:
                    base_down = 4 * ((i + 1) * n + j)
                    union(base + 2, base_down + 0)
            
        return cnt

grid = [" /","/ "]
print(Solution().regionsBySlashes(grid))
def longest_possible_route(mat, xs, ys, xd, yd):
    n = len(mat)
    m = len(mat[0])
    best = [0]
    visited = [[False] * m for _ in range(n)]

    def back(x, y,steps):
        if x == xd and y == yd:
            best[0] = max(best[0], steps)
            return

        if x < 0 or y < 0 or x >= n or y >= m:
            return
        
        if visited[x][y] or mat[x][y] == 0:
            return
        
        visited[x][y] = 1
        back(x + 1, y, steps + 1)
        back(x, y + 1, steps + 1)
        back(x - 1, y, steps + 1)
        back(x, y - 1, steps + 1)
        visited[x][y] = 0
        return

    back(xs, ys, 0)
    if (best[0] == 0):
        return -1
    return best[0]
    
xs = 0
ys = 0
xd = 1
yd = 7
mat = [ [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

print(longest_possible_route(mat, xs, ys, xd, yd))
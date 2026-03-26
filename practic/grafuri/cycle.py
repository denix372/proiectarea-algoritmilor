
def solve(n, m, a):
    if a[0][0] == 0:
        return 0
    
    visited = [[False] * m for _ in range(n)]
    depth = [[0] * m for _ in range(n)]
    ok = 0
    def dfs(x, y, px, py, d):
        nonlocal ok
        visited[x][y]  = True
        depth[x][y] = d
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1 and not (nx == px and ny == py):
                    if not visited[nx][ny]:
                        dfs(nx, ny, x, y, d + 1)
                    else:
                        #ciclu
                        if nx == 0 and ny == 0 and d >= 2:
                            ok = 1
    dfs(0, 0, -1, -1, 0)
    return ok
    


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    print(solve(n, m, a))
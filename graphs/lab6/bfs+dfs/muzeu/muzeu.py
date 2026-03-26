from collections import deque
INF = 10**9

def muzeu(n, grid):
    dist = [[INF] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'P':
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for ox, oy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + ox
            ny = y + oy

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '#':
                if dist[x][y] + 1 < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist

with open("muzeu.in") as fin:
    n = int(fin.readline())
    grid = [list(fin.readline()) for _ in range(n)]

dist = muzeu(n, grid)

with open("muzeu.out", "w") as fout:
    for i in range(n):
        line = []
        for j in range(n):
            if grid[i][j] == '#':
                line.append("-2")
            elif dist[i][j] == INF:
                line.append("-1")
            else:
                line.append(str(dist[i][j]))
        fout.write(" ".join(line) + "\n")
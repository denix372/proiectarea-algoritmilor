from collections import deque

def muzeu_bfs(N, grid):
    INF = 10**9
    dist = [[INF] * N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'P':
                dist[i][j] = 0
                q.append((i, j))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < N and grid[xx][yy] != '#':
                if dist[x][y] + 1 < dist[xx][yy]:
                    dist[xx][yy] = dist[x][y] + 1
                    q.append((xx, yy))

    return dist


with open("muzeu.in") as fin:
    N = int(fin.readline().strip())
    grid = [list(fin.readline().strip()) for _ in range(N)]

dist = muzeu_bfs(N, grid)

with open("muzeu.out", "w") as fout:
    for i in range(N):
        line = []
        for j in range(N):
            if grid[i][j] == '#':
                line.append("-1")
            else:
                if dist[i][j] == 10**9:
                    line.append("-1")
                else:
                    line.append(str(dist[i][j]))
        fout.write(" ".join(line) + "\n")

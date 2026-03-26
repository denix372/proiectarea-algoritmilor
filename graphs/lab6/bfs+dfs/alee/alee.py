from collections import deque

def lee_bfs(N, trees, start, end):
    # grid 1-based, exact ca în C++
    a = [[0] * (N + 1) for _ in range(N + 1)]
    for x, y in trees:
        a[x][y] = 1  # copac = obstacol

    INF = 10**9
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    sx, sy = start
    ex, ey = end

    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 1  # EXACT ca în C++

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            # aceleași condiții ca în C++
            if xx < 1 or xx > N or yy < 1 or yy > N:
                continue
            if a[xx][yy] == 1:
                continue

            if dist[x][y] + 1 < dist[xx][yy]:
                dist[xx][yy] = dist[x][y] + 1
                q.append((xx, yy))

    return dist[ex][ey]


# citire + scriere în fișiere
with open("alee.in") as fin:
    N, M = map(int, fin.readline().split())
    trees = [tuple(map(int, fin.readline().split())) for _ in range(M)]
    x1, y1, x2, y2 = map(int, fin.readline().split())

res = lee_bfs(N, trees, (x1, y1), (x2, y2))

with open("alee.out", "w") as fout:
    fout.write(str(res))

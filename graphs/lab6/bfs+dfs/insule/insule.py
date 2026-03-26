from collections import deque

# BFS pentru componente conexe (numărare insule)
def bfs_component(N, M, grid, si, sj, visited):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = True
    val = grid[si][sj]

    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            xx, yy = x + dx, y + dy
            if 0 <= xx < N and 0 <= yy < M:
                if not visited[xx][yy] and grid[xx][yy] == val:
                    visited[xx][yy] = True
                    q.append((xx, yy))


# BFS pentru pod minim între R și G
def bfs_bridge(N, M, grid, sources, targets):
    INF = 10**9
    dist = [[INF] * M for _ in range(N)]
    q = deque()

    # inițializare surse
    for x, y in sources:
        dist[x][y] = 0
        q.append((x, y))

    targets = set(targets)

    while q:
        x, y = q.popleft()

        if (x, y) in targets:
            return dist[x][y] + 1

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            xx, yy = x + dx, y + dy
            if 0 <= xx < N and 0 <= yy < M:
                # podul merge DOAR prin apă
                if grid[xx][yy] == 0 and dist[x][y] + 1 < dist[xx][yy]:
                    dist[xx][yy] = dist[x][y] + 1
                    q.append((xx, yy))

    return -1


with open("insule.in", "r") as fin:
    N, M = map(int, fin.readline().split())
    grid = [list(map(int, list(fin.readline().strip()))) for _ in range(N)]

# 1) Numărăm insulele
visited = [[False] * M for _ in range(N)]
NR = NG = NB = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and grid[i][j] in (1, 2, 3):
            if grid[i][j] == 1:
                NR += 1
            elif grid[i][j] == 2:
                NG += 1
            else:
                NB += 1
            bfs_component(N, M, grid, i, j, visited)

# 2) Construim sursele și țintele pentru pod
sources = []  # R + apă adiacentă R
targets = []  # G + apă adiacentă G

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:  # R
            sources.append((i, j))
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                xx, yy = i + dx, j + dy
                if 0 <= xx < N and 0 <= yy < M and grid[xx][yy] == 0:
                    sources.append((xx, yy))

        if grid[i][j] == 2:  # G
            targets.append((i, j))
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                xx, yy = i + dx, j + dy
                if 0 <= xx < N and 0 <= yy < M and grid[xx][yy] == 0:
                    targets.append((xx, yy))

# 3) BFS pentru pod minim
Lg = bfs_bridge(N, M, grid, sources, targets)

with open("insule.out", "w") as fout:
    fout.write(f"{NR} {NG} {NB} {Lg}")

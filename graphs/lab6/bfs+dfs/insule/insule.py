from collections import deque
INF = 10**9

# BFS for connected components (counting islands)
def bfs_component(N, M, grid, x1, y1, visited):
    q = deque()
    q.append((x1, y1))
    visited[x1][y1] = True

    while q:
        x, y = q.popleft()
        for ox, oy in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
            nx = x + ox
            ny = y + oy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and grid[nx][ny] == grid[x1][y1]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

# BFS for minimum bridge between R and G
def bfs_bridge(N, M, grid, sources, targets):
    dist = [[INF] * M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    q = deque()

    for x, y in sources:
        dist[x][y] = 0
        visited[x][y] = True
        q.append((x, y))

    targets = set(targets)

    while q:
        x, y = q.popleft()

        # reached a target cell -> bridge found
        if (x, y) in targets:
            return dist[x][y] + 1

        for ox, oy in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
            nx = x + ox
            ny = y + oy
            if 0 <= nx < N and 0 <= ny < M:
                # the bridge can only go through water
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return -1

with open("insule.in", "r") as fin:
    N, M = map(int, fin.readline().split())
    grid = [list(map(int, list(fin.readline().strip()))) for _ in range(N)]

# 1) Count islands
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

# 2) Build sources and targets for the bridge
sources = []  # R + water adjacent to R
targets = []  # G + water adjacent to G

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:  # R
            sources.append((i, j))
            for ox, oy in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
                nx = i + ox
                ny = j + oy
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                    sources.append((nx, ny))

        if grid[i][j] == 2:  # G
            targets.append((i, j))
            for ox, oy in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
                nx = i + ox
                ny = j + oy
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                    targets.append((nx, ny))

# 3) BFS for minimum bridge
Lg = bfs_bridge(N, M, grid, sources, targets)

with open("insule.out", "w") as fout:
    fout.write(f"{NR} {NG} {NB} {Lg}")

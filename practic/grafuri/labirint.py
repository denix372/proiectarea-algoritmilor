from collections import deque

    

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]

portals = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            sx = i
            sy = j
        if a[i][j] == 'D':
            dx = i
            dy = j
        if a[i][j] == 'P':
            portals.append((i, j))
    
dist = [[-1] * m for _ in range(n)]
q = deque()
q.append((sx, sy))
dist[sx][sy] = 0

teleported = False
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    x, y = q.popleft()

    if (x, y) == (dx, dy):
        print(dist[x][y])
        exit()

    if a[x][y] == 'P' and not teleported:
        teleported = True
        for px, py in portals:
            if (px, py) == (x, y):
                continue
            if dist[px][py] == -1:
                dist[px][py] = dist[x][y] 
                q.append((px, py))

    for dx2, dy2 in dirs:
        nx, ny = x + dx2, y + dy2
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] != 'X' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

print(-1)
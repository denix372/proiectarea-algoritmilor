from collections import deque
INF = 10**9

n, m = map(int, input().split())
a = [[0] * n for _ in range(n)]
for _ in range(m):
    x, b = map(int, input().split())
    a[x - 1][b - 1] = 1

x1, y1, x2, y2 = map(int, input().split())

def solve(n, m, a):
    dist = [[INF] * n for _ in range(n)]
    dist[x1 - 1][y1 - 1] = 1
    q = deque([(x1 - 1, y1 - 1)])
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] != 1 and dist[nx][ny] == INF:
                    dist[nx][ny] = 1 + dist[x][y]
                    q.append((nx, ny))
    print(dist[x2 - 1][y2 - 1])

solve(n, m, a)
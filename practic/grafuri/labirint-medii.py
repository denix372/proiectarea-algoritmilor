from collections import deque
INF = 10**9
def solve(n, m, a):
    d = [[INF] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'G':
                d[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] != 'X':
                    if d[nx][ny] > d[x][y] + 1:
                        d[nx][ny] = d[x][y] + 1
                        q.append((nx, ny))
        if x == n - 1 or x == 0:
            nx = n - 1 - x
            ny = y
            if a[nx][ny] != 'X':
                if d[nx][ny] > d[x][y] + 1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))
        if y == m - 1 or y == 0:
            ny = m - 1 - y
            nx = x
            if a[nx][ny] != 'X':
                if d[nx][ny] > d[x][y] + 1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if d[i][j] >= INF:
                print(-1, end = " ")
            else:
                print(d[i][j], end =" ")
        print()
    
n, m = map(int, input().split())
a = [input() for _ in range(n)]
solve(n,m, a)
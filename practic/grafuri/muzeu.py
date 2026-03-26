from collections import deque
INF = 10**9
def solve(n, a):
    dist =[[INF] * n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'P':
                dist[i][j] = 0
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1),(-1, 0), (0, -1)]:
            nx = x + dx 
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] != '#' and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    for i in range(n):
        for j in range(n):
            if a[i][j] == '#':
                print(-2, end = " ")
            elif dist[i][j] == INF:
                print(-1, end  = " ")
            else:
                print(dist[i][j], end = " ")
        print()           

n = int(input())
a = [input().strip() for _ in range(n)]
solve(n, a)
from collections import deque
from heapq import heappop, heappush
INF = 10**9
def solve(n, a):
    q = []
    heappush(q, (a[0][0], (0, 0)))
    dist = [[INF] * n for _ in range(2)]
    dist[0][0] = a[0][0]
    while q:
        d, (x, y) = heappop(q)
        if d != dist[x][y]:
            continue
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0)]: 
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 2 and 0 <= ny < n:
                if a[nx][ny] != -1:
                    if d + a[nx][ny] < dist[nx][ny]:
                        dist[nx][ny] = d + a[nx][ny]
                        heappush(q, (dist[nx][ny], (nx, ny)))
    print(dist[1][n - 1])
        
n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
solve(n, a)
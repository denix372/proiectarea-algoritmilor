
from heapq import heappush, heappop
INF = 10 ** 6

def max_path(grid):
    n = len(grid)
    dist = [[-INF] * n for _ in range(n)]
    dist[0][0] = grid[0][0]
    q = []
    heappush(q, (-grid[0][0], (0, 0)))
    while q:
        d, (x, y) = heappop(q)

        if -d < dist[x][y]:
            continue

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                m = min(dist[x][y], grid[nx][ny]) 
                if m > dist[nx][ny]:
                    dist[nx][ny] = m 
                    heappush(q, (-dist[nx][ny], (nx, ny)))
    return dist[n - 1][n - 1]

grid = [[5, 4, 5],
        [1, 6, 1],
        [7, 8, 9]]
print(max_path(grid))
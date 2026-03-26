from collections import deque
INF = 10**9

def alee(n, trees, x1, y1, x2, y2):
    a = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y in trees:
        a[x][y] = 1
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    dist[x1][y1] = 1
    q = deque()
    q.append((x1, y1))

    while q:
        x, y = q.popleft()

        for ox, oy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + ox
            ny = y + oy 
        
            if 1 <= nx <= n and 1 <= ny <= n and a[nx][ny] != 1:
                if dist[x][y] + 1 < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist[x2][y2]


with open("alee.in", "r") as fin:
    n, m = map(int, fin.readline().split())
    trees = []
    for _ in range(m):
        x, y = map(int, fin.readline().split())
        trees.append((x, y))
    x1, y1, x2, y2 = map(int, fin.readline().split())

res = alee(n, trees, x1, y1, x2, y2)

with open("alee.out", "w") as fout:
    fout.write(str(res))

INF = 10**8
def floydWarshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j],
                                     dist[i][k] + dist[k][j])

dist = [[0, 4, INF, 5, INF],
            [INF, 0, 1, INF, 6],
            [2, INF, 0, 3, INF],
            [INF, INF, 1, 0, 2],
            [1, INF, INF, 4, 0]]
    
floydWarshall(dist)

for row in dist:
    print(*row)
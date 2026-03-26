import heapq
INF = 10**9
def dijkstra(adj, src):
    v = len(adj)
    q = []
    dist = [INF] * v
    dist[src] = 0
    heapq.heappush(q, (0, src))

    while q:
        d, u = heapq.heappop(q)
        if d > dist[u]:
            continue
        
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(q, (dist[v], v))
    return dist

src = 0
adj = [
    [(1, 4), (2, 8)],
    [(0, 4), (4, 6), (2, 3)],
    [(0, 8), (3, 2), (1, 3)],
    [(2, 2), (4, 10)],
    [(1, 6), (3, 10)]
]

res = dijkstra(adj, src)
print(*res)
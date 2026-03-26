from heapq import heappush, heappop
INF = 10**15
def shortest_routes(n, adj):
    q = []
    heappush(q, (0, 1))
    dist = [INF] * (n + 1)
    dist[1] = 0
    while q:
        d, u = heappop(q)
        if d > dist[u]:
            continue
    
        for v,w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] =dist[u] + w
                heappush(q, (dist[v], v))
    return dist[1:]

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))

dist = shortest_routes(n, adj)
print(*dist)
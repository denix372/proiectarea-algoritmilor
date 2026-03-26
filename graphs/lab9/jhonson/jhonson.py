from heapq import heappop, heappush

INF = 10**18

def bellman_ford(n, edges, s):
    dist = [INF] * (n + 1)
    dist[s] = 0
    for _ in range(n):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # negative cycle detecting
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None
    return dist

def dijkstra(n, adj, src):
    dist = [INF] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(pq, (dist[v], v))
    return dist

def johnson(n, edges):
    # 1. add node s = n
    s = n
    new_edges = edges + [(s, u, 0) for u in range(n)]

    # 2. Bellman-Ford
    h = bellman_ford(n, new_edges, s)
    if h is None:
        return None  # negative cycle

    h = h[:n]
    # 3. repondering
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        w2 = w + h[u] - h[v]
        adj[u].append((v, w2))

    # 4. Dijkstra on each node
    dist = [[INF]*n for _ in range(n)]
    for u in range(n):
        d = dijkstra(n, adj, u)
        for v in range(n):
            dist[u][v] = d[v] - h[u] + h[v]

    return dist

V = 4
edgeList = [
    (0, 1, -5),
    (0, 2, 2),
    (0, 3, 3),
    (1, 2, 4),
    (2, 3, 1)
]
dist = johnson(V, edgeList)
for r in dist:
    print(*("INF" if x >= INF//2 else x for x in r))
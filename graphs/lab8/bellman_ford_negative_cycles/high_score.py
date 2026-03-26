
from collections import deque
INF = 10**18
def solve(n, m, edges):
    dist = [INF] * n
    dist[0] = 0
    for _ in range(n):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    q = deque()
    for u, v, w in edges:
        if dist[u]!= INF and dist[u] + w < dist[v]:
            q.append(v)

    adj = [[] for _ in range(n)]
    for a, b, _ in edges:
        adj[a].append(b)
    
    visited = [False] * n
    while q:
        u = q.popleft()
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                q.append(v)
    if visited[n - 1]:
        return -1
    return -dist[n - 1]


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((a - 1, b - 1, - w))
print(solve(n, m , edges))
def ford_fulkerson(n, adj, s, t):
    residual = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, cap in adj[u]:
            residual[u][v] = cap

    def dfs(u, t, flow, visited):
        if u == t:
            return flow
        visited[u] = True
        for v in range(n):
            if not visited[v] and residual[u][v] > 0:
                pushed = dfs(v, t, min(flow, residual[u][v]), visited)
                if pushed > 0:
                    residual[u][v] -= pushed
                    residual[v][u] += pushed
                    return pushed
        return 0
    max_flow = 0
    while True:
        visited = [False] * n
        pushed = dfs(s, t, float("inf"), visited)
        if pushed == 0:
            break
        max_flow += pushed

    return max_flow

n = 6
edges = [
    (0, 1, 16),
    (0, 2, 13),
    (1, 2, 10),
    (2, 1, 4),
    (1, 3, 12),
    (3, 2, 9),
    (2, 4, 14),
    (4, 3, 7),
    (3, 5, 20),
    (4, 5, 4)
]
adj = [[] for _ in range(n)]
for a, b, w in edges:
    adj[a].append((b, w))

print(ford_fulkerson(n, adj, 0, 5))
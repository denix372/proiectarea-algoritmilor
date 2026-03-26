from collections import deque

def edmonds_karp(n, adj, s, t):
    residual = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, cap in adj[u]:
            residual[u][v] = cap

    def bfs():
        parent = [-1] * n
        parent[s] = -2 #source
        q = deque([(s, float("inf"))])

        while q:
            u, flow = q.popleft()
            for v in range(n):
                if parent[v] == -1 and residual[u][v] > 0:
                    parent[v] = u
                    new_flow = min(flow, residual[u][v])
                    if v == t:
                        return new_flow, parent
                    q.append((v, new_flow))
        return 0, parent
    max_flow = 0
    while True:
        flow, parent = bfs()
        if flow == 0:
            break
        max_flow += flow
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= flow
            residual[v][u] += flow
            v = u
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
    (4, 5, 4)]
adj = [[] for _ in range(n)]
for a, b, w in edges:
    adj[a].append((b, w))

print(edmonds_karp(n, adj, 0, 5))
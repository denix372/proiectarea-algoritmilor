import sys
input = sys.stdin.readline
from collections import deque

def edmonds_karp(n, adj, s, t, edges):
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
    print(max_flow)

    visited = [False] * n
    q = deque([0])
    visited[0] = True
    while q:
        u = q.popleft()
        for v in range(n):
            if residual[u][v] > 0 and not visited[v]:
                visited[v] = True
                q.append(v)

    for a, b in edges:
        if visited[a] and not visited[b] and residual[a][b] == 0:
            print(a + 1, b + 1)
        if visited[b] and not visited[a] and residual[b][a] == 0:
            print(b + 1, a + 1)

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append((b - 1, 1))
    adj[b - 1].append((a - 1, 1))
    edges.append((a - 1, b - 1))

edmonds_karp(n, adj, 0, n - 1, edges)
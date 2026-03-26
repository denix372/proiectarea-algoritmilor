import sys
input = sys.stdin.readline
from collections import deque

INF = 10**15

def edmonds_karp(n, adj, s, t):
    residual = [[0] * n for _ in range(n)]
    neighbors = [set() for _ in range(n)]
    
    for u in range(n):
        for v, cap in adj[u]:
            residual[u][v] += cap
            neighbors[u].add(v)
            neighbors[v].add(u)
            
    neighbors = [list(nx) for nx in neighbors]

    def bfs(limit):
        parent = [-1] * n
        parent[s] = -2
        q = deque([(s, INF)])

        while q:
            u, flow = q.popleft()
            for v, _ in adj[u]:
                if parent[v] == -1 and residual[u][v] >= limit:
                    parent[v] = u
                    new_flow = min(flow, residual[u][v])
                    if v == t:
                        return new_flow, parent
                    q.append((v, new_flow))
        return 0, parent

    max_flow = 0
    limit = 1 << 30
    
    while limit > 0:
        flow, parent = bfs(limit)
        if flow == 0:
            limit //= 2
            continue
            
        max_flow += flow
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= flow
            residual[v][u] += flow
            v = u
            
    return max_flow

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a - 1].append((b - 1, w))
    adj[b - 1].append((a - 1, w))

print(edmonds_karp(n, adj, 0, n - 1))
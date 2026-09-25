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

def solve(graph):
    n = len(graph)
    # Convert Adjacency Matrix to Adjacency List for Edmonds-Karp
    adj = [[] for _ in range(n)]
    
    for u in range(n):
        for v in range(n):
            if graph[u][v] == 1:
                # Assign a strict capacity of 1 to guarantee edge-disjoint paths
                adj[u].append((v, 1))
                
    # Edge-Disjoint Paths = Max Flow in a graph with unit capacities
    return edmonds_karp(n, adj, source, sink)

graph = [[0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0]]

source = 0
sink = 7
result = solve(graph, source, sink)
print(f"Maximum number of edge-disjoint paths from {source} to {sink}: {result}")

from collections import deque

def edmonds_karp(n, adj, s, t):
    residual = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, cap in adj[u]:
            residual[u][v] = cap

    def bfs():
        parent = [-1] * n
        parent[s] = -2 
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


def solve(graph: list[list[int]]) -> int:
    # Minnr of edges to disconnect = Min Cut = Max Flow
    n = len(graph)
    
    adj = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if graph[u][v] == 1:
                adj[u].append((v, 1))
                
    global_min_cut = float('inf')
    
    s = 0
    for t in range(1, n):
        current_cut = edmonds_karp(n, adj, s, t)
        global_min_cut = min(global_min_cut, current_cut)
        
    return global_min_cut

graph_matrix = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

print(f"Minimum Number of Edges to Remove: {solve(graph_matrix)}")

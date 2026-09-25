from collections import deque

def edmonds_karp(n, adj, s, t):
    residual = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, cap in adj[u]:
            residual[u][v] = cap

    def bfs():
        parent = [-1] * n
        parent[s] = -2  # Source marker
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

def solve(n: int, edges: list[tuple[int, int]], s: int, t: int) -> int:
    # NODE SPLITTING: 
    # Every node 'i' becomes two virtual nodes to bottleneck the flow.
    # We map them as:
    # node_in = i
    # node_out = i + n
    
    # The transformed graph will have 2 * n nodes
    total_nodes = 2 * n
    adj = [[] for _ in range(total_nodes)]
    
    # 1. Add internal edges: node_in -> node_out
    for i in range(n):
        node_in = i
        node_out = i + n
        
        if i == s or i == t:
            # Source and Sink can be part of multiple paths, so no bottleneck
            adj[node_in].append((node_out, float('inf')))
        else:
            # Intermediate nodes can only be traversed ONCE (capacity = 1)
            adj[node_in].append((node_out, 1))
            
    # 2. Add original graph edges: u_out -> v_in
    for u, v in edges:
        u_out = u + n
        v_in = v
        
        # The capacity here can be 1 (or infinity), because the flow 
        # is already bottlenecked by the internal node_in -> node_out edges
        adj[u_out].append((v_in, 1))
        
    # Find Max Flow in the doubled graph.
    # We start strictly from the 'in' state of the source 
    # and want to reach the 'out' state of the sink.
    s_in = s
    t_out = t + n
    
    return edmonds_karp(total_nodes, adj, s_in, t_out)

# "Hourglass" / Bottleneck Graph Example
# 0 -> 1 and 0 -> 2
# 1 -> 3 and 2 -> 3 (Node 3 is the bottleneck)
# 3 -> 4 and 3 -> 5
# 4 -> 6 and 5 -> 6 (Destination is 6)

n = 7
edges = [
    (0, 1), (0, 2),
    (1, 3), (2, 3),
    (3, 4), (3, 5),
    (4, 6), (5, 6)
]
source = 0
sink = 6

print("Hourglass Graph Analysis:")
# Edge-Disjoint paths on this graph would return 2 (0-1-3-4-6 and 0-2-3-5-6)
# Vertex-Disjoint returns 1, because the paths collide at Node 3.
result = solve(n, edges, source, sink)
print(f"Maximum number of Vertex-Disjoint paths from {source} to {sink} is: {result}")
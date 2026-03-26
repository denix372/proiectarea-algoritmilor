from collections import deque

def push_relable(n, adj, s, t):
    residual = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, cap in adj[u]:
            residual[u][v] = cap
    
    height = [0] * n
    excess = [0] * n
    height[s] = n

    for v, cap in adj[s]:
        residual[s][v] -= cap
        residual[v][s] += cap
        excess[v] += cap
        excess[s] -= cap
    
    active = deque()
    for u in range(n):
        if u != s and u != t and excess[u] > 0:
            active.append(u)

    def push(u, v):
        delta = min(excess[u], residual[u][v])
        residual[u][v] -= delta
        residual[v][u] += delta
        excess[u] -= delta
        excess[v] += delta
        if excess[v] > 0 and v != s and v != t and v not in active:
            active.append(v)

    def relabel(u):
        min_h = float("inf")
        for v in range(n):
            if residual[u][v] > 0:
                min_h = min(min_h, height[v])
        height[u] = min_h + 1

   
    while active:
        u = active[0]
        pushed = False
        for v in range(n):
            if residual[u][v] > 0 and height[u] == height[v] + 1:
                push(u, v)
                pushed = True
                if excess[u] == 0:
                    active.popleft()
                break
            if not pushed:
                relabel(u)
    return excess[t]

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

print(push_relable(n, adj, 0, 5))
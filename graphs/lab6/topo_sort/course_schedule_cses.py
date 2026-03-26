from collections import deque

def kahn(n, adj, indeg):
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indeg[b] += 1

order = kahn(n, adj, indeg)
if len(order) != n:
    print("IMPOSSIBLE")
else: 
    print(*order)
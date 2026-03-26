from collections import deque
INF = 10**9

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
indeg = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    indeg[b - 1] += 1

q = deque()
for i in range(n):
    if indeg[i] == 0:
        q.append(i)
    
topo = []
while q:
    u = q.popleft()
    topo.append(u + 1)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
if len(topo) != n:
    print("IMPOSSIBLE")
else:
    print(*topo)
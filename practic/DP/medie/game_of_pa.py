from collections import deque
INF = 10**9

n, m = map(int, input().split())
r = list(map(int, input().split()))
p = list(map(int, input().split()))
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
    topo.append(u)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

dpr = r.copy()
dpp = p.copy()

for u in topo:
    for v in adj[u]:
        if dpr[u] + r[v] > dpr[v]:
            dpr[v] = dpr[u] + r[v]
            dpp[v] = max(p[v], dpp[u])
        elif dpr[u] + r[v] == dpr[v]:
            dpp[v] = min(dpp[v], max(p[v], dpp[u]))

max_r = -INF
min_p = INF
for i in range(n):
    if dpr[i] > max_r:
        max_r = dpr[i]
        min_p = dpp[i]
    elif dpr[i] == max_r:
        min_p = min(min_p, dpp[i])
        
print(max_r, min_p)
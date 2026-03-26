from heapq import heappush, heappop
INF = 10**9

n, m, k = map(int, input().split())
fort = list(map(int, input().split()))
for i in range(len(fort)):
    fort[i] -= 1
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a - 1].append((b - 1, w))
    adj[b - 1].append((a - 1, w))

q = []
dist = [INF] * n
res = [-1] * n
for s in fort:
    heappush(q, (0, s, s))
    res[s] = s
    dist[s] = 0

while q:
    d, u, f = heappop(q)
    if d > dist[u]:
        continue
    for v,w in adj[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            res[v] = f
            heappush(q, (dist[v], v, f))
        elif dist[u] + w == dist[v]:
            res[v] = min(res[v], f)
fort_set = set(fort)
for i in range(n):
    if i in fort_set:
        print(0, end=" ")
    elif res[i] == -1:
        print(0, end=" ")
    else:
        print(res[i] + 1, end=" ")
print()

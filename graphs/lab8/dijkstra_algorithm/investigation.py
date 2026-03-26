INF = 10**18
MOD = 10**9 + 7
from heapq import heappush, heappop
def investigation(n, adj):
    q =[]
    heappush(q, (0, 1))

    dist = [INF] * (n + 1)
    maxf = [0] * (n + 1)
    minf = [INF] * (n + 1)
    ways = [0] * (n + 1)
    dist[1] = 0
    minf[1] = 0
    maxf[1] = 0
    ways[1] = 1
    
    while q:
        d, u = heappop(q)
        if d > dist[u]:
            continue

        for v, w in adj[u]:
            m = dist[u] + w 
            if m < dist[v]:
                dist[v] = m
                ways[v] = ways[u]
                minf[v] = minf[u] + 1
                maxf[v] = maxf[u] + 1
                heappush(q, (dist[v], v))
            elif m == dist[v]:
                ways[v] = (ways[v] + ways[u]) % MOD
                minf[v] = min(minf[v], minf[u] + 1)
                maxf[v] = max(maxf[v], maxf[u] + 1)

    print(dist[n], ways[n], minf[n], maxf[n])

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))

investigation(n, adj)
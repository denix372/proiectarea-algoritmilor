from heapq import heappush, heappop

INF = 10**9
t  = int(input())

for _ in range(t):
    n, m, s = map(int, input().split())
    calc = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a - 1].append((b - 1, c))
        adj[b - 1].append((a - 1, c))

    dist = [INF] * n
    dist[s - 1] = 0
    q = []
    heappush(q, (dist[s - 1], s - 1))
    while q:
        d, u = heappop(q)
        if d > dist[u]:
            continue
        for v,w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(q, (dist[v], v))

    if dist == calc:
        print("DA")
    else:
        print("NU")
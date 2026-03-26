import sys
input = sys.stdin.readline
from heapq import heappush, heappop
INF= 10**14 + 1
def flight(n, adj):
    dist = [[INF, INF]  for _ in range(n + 1)]
    dist[1][0] = 0
    q = []
    heappush(q, (dist[1][0], 1, 0))

    while q:
        d, u, ok = heappop(q)
        if d != dist[u][ok]:
            continue

        for v, w in adj[u]:
            m1 = dist[u][ok] + w 
            if m1 < dist[v][ok]:
                dist[v][ok] = m1
                heappush(q, (dist[v][ok], v, ok))
            if ok == 0:
                m2 = dist[u][ok] + w // 2
                if m2 < dist[v][1]:
                    dist[v][1] = m2
                    heappush(q, (dist[v][1], v, 1))
    return dist[n][1]

def flight_discount_cses(n, adj, rev):
    # Dijkstra 1: Shortest paths from the start node (1)
    dist1 = [INF] * (n + 1)
    dist1[1] = 0
    q1 = [(0, 1)]
    while q1:
        d, u = heappop(q1)
        if d > dist1[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist1[v]:
                dist1[v] = d + w
                heappush(q1, (dist1[v], v))

    # Dijkstra 2: Shortest paths to the end node (n) on reversed graph
    dist2 = [INF] * (n + 1)
    dist2[n] = 0
    q2 = [(0, n)]
    while q2:
        d, u = heappop(q2)
        if d > dist2[u]:
            continue
        for v, w in rev[u]:
            if d + w < dist2[v]:
                dist2[v] = d + w
                heappush(q2, (dist2[v], v))

    # Iterate all edges to find the optimal single discount
    ans = INF
    for u in range(1, n + 1):
        if dist1[u] == INF:
            continue
        d1_u = dist1[u]
        for v, w in adj[u]:
            if dist2[v] != INF:
                cost = d1_u + w // 2 + dist2[v]
                if cost < ans:
                    ans = cost

    return ans

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
rev = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    adj[a].append((b, w))
    rev[b].append((a, w))

print(flight_discount_cses(n, adj, rev))


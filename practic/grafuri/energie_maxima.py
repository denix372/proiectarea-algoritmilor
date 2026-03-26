from heapq import heappush, heappop
INF = 10**9
E = 2.71828182846
import math
def f(x):
    return 2 / (1 + E**(-x)) - 1

def solve(n, m, e, adj):
    dist = [0] * n
    dist[0] = e
    q = []
    heappush(q, (-e, 0))
    while q:
        d, u = heappop(q)
        for v,p in adj[u]:
            m = dist[u] * (1 - f(math.log(p)))
            if m > dist[v]:
                dist[v] = m
                heappush(q, (-dist[v], v))

    print(int(dist[n - 1]))

n, m, e = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    s = input().split()
    i, j, p = int(s[0]), int(s[1]), float(s[2])
    adj[i - 1].append((j - 1, p))

solve(n, m, e, adj)


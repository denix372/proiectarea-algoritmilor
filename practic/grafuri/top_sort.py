from collections import deque
from heapq import heappush, heappop

n, m = map(int, input().split())
v = [0] * n
adj = [[] for _ in range(n)]
indeg = [0] * n

for i in range(n):
    v[i] = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    indeg[b - 1] += 1

q = []
for i in range(n):
    if indeg[i] == 0:
        heappush(q, (v[i], i))

topo = []
while q:
    wu, u = heappop(q)
    topo.append(u + 1)
    for u2 in adj[u]:
        indeg[u2] -= 1
        if indeg[u2] == 0:
            heappush(q, (v[u2], u2))
print(*topo)

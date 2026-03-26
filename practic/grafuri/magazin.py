from heapq import heappush, heappop
INF = 1000

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    x, y, c = map(int, input().split())
    adj[x - 1].append((y - 1, c))
    adj[y - 1].append((x - 1, c))

na, nm =  map(int, input().split())
ap = list(map(int, input().split()))
for i in range(na):
    ap[i] -= 1
mg = list(map(int, input().split()))
for i in range(nm):
    mg[i] -= 1

dist = [INF] * n
q = []
shop = [-1] * n
for z in mg:
    dist[z] = 0
    shop[z] = z
    heappush(q, (0, z, z))

while q:
    d, u, z = heappop(q)
    if d != dist[u]:
        continue
    
    for v, w in adj[u]:
        
        if d + w < dist[v]:
            dist[v] = d + w
            shop[v] = z
            heappush(q, (dist[v], v, z))
        elif d + w == dist[v]:
            shop[v] = min(shop[v], z)

for a in ap:
    if dist[a] >= INF:
        print(0, end = " ")
    else:
        print(shop[a] + 1, end = " ")
print()


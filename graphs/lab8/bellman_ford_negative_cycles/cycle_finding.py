INF = 10**8
def find_cycle(n, edges):
    dist = [INF] * (n + 1)
    p = [-1] * (n + 1)
    dist[1] =  0
    x = -1
    for i in range(n):
        x = -1
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                p[v] = u
                x = v
    if x == -1:
        print("NO")
        return
    for _ in range(n):
        x = p[x]
    cycle = []
    u = x
    while True:
        cycle.append(u)
        u = p[u]
        if u == x:
            cycle.append(u)
            break
    print("YES")
    print(*cycle[::-1])


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))
find_cycle(n, edges)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
 
def union(parent, rank, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
 
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True
 
def kruskal(n, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    cnt = 0
    cost = 0
 
    edges.sort(key = lambda x : x[2])
 
    for u, v, w in edges:
        if union(parent, rank, u, v):
            cost += w
            cnt += 1
            if cnt == n - 1:
                return cost
    return -1
 
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
x = kruskal(n, edges)
if x == -1:
    print("IMPOSSIBLE")
else:
    print(x)

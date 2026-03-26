def find (parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union_by_rank(parent, rank, a, b):
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

def kruskal_by_rank(n, edges):
    parent = list(range(n))
    rank = [0] * n
    mst = []
    cost = 0
    
    edges.sort(key = lambda x: x[2])

    for u, v, w in edges:
        if union_by_rank(parent, rank, u, v):
            cost += w
            mst.append((u, v, w))
            if len(mst) == n - 1:
                break
    return cost, mst

def union_by_size(parent, size, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
    if ra == rb:
        return False
    
    if size[ra] < size[rb]:
        parent[ra] = rb
        size[rb] += size[ra]
    else:
        parent[rb] = ra
        size[ra] += size[rb]
    return True

def kruskal_by_size(n, edges):
    parent = list(range(n))
    rank = [1] * n # every set has 1 node
    mst = []
    cost = 0
    
    edges.sort(key = lambda x: x[2])

    for u, v, w in edges:
        if union_by_size(parent, rank, u, v):
            cost += w
            mst.append((u, v, w))
            if len(mst) == n - 1:
                break
    return cost, mst

n = 4
edges = [
    (0, 1, 1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (2, 3, 5)
]

cost, mst = kruskal_by_rank(n, edges)
cost2, mst2 = kruskal_by_size(n, edges)

print("Cost:", cost)
print("MST:", mst)
print("-----------------")
print("Cost:", cost2)
print("MST:", mst2)

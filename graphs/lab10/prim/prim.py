from heapq import heappush, heappop

def prim(n, adj):
    visited = [False] * n
    q = []
    mst = []
    cost = 0
    
    visited[0] = True
    for v, w in adj[0]:
        heappush(q, (w, 0, v))
    
    while q and len(mst) < n - 1:
        w, u, v = heappop(q)
        if visited[v]:
            continue
        
        visited[v] = True
        mst.append((u, v, w))
        cost += w
        for nv, nw in adj[v]:
            if not visited[nv]:
                heappush(q, (nw, v, nv))
    return cost, mst

n = 4
adj = [
    [(1, 1), (2, 4)],
    [(0, 1), (2, 3), (3, 2)],
    [(0, 4), (1, 3), (3, 5)],
    [(1, 2), (2, 5)]
]

cost, mst = prim(n, adj)
print("Cost:", cost)
print("MST:", mst)

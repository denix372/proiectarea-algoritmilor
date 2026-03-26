from heapq import heappush, heappop
from math import log

def minimumProductMST(graph):
    n = len(graph)
    visited = [False] * n
    q = []
    mst = []
    min_product = 1

    visited[0] = True
    for v in range(n):
        weight = graph[0][v]
        if weight > 0:
            heappush(q, (log(weight), weight, 0, v))

    while q and len(mst) < n - 1:
        _, w, u, v = heappop(q)
        
        if visited[v]:
            continue

        visited[v] = True
        min_product *= w
        mst.append((u, v, w))
        

        for next_v in range(n):
            next_w = graph[v][next_v]
            if next_w > 0 and not visited[next_v]:
                heappush(q, (log(next_w), next_w, v, next_v))
    
    return min_product, mst

if __name__=='__main__':
    graph = [ [ 0, 2, 0, 6, 0 ], 
              [ 2, 0, 3, 8, 5 ], 
              [ 0, 3, 0, 0, 7 ], 
              [ 6, 8, 0, 0, 9 ], 
              [ 0, 5, 7, 9, 0 ], ]

    min_product, mst = minimumProductMST(graph)
    print("Minimum Product:", min_product)
    print("MST Edges (u, v, weight):")
    for u, v, w in mst:
        print(f"Edge {u} - {v} with weight {w}")
import sys
from heapq import heappush, heappop
INF = 10**15

#regular approach
def shortest_routes_ii_2():
    n, m, q = map(int, input().split())
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        dist[a][b] = min(dist[a][b], w)
        dist[b][a] = min(dist[b][a], w)
 
    for i in range(1, n + 1):
        dist[i][i] = 0
 
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    shortest_routes_ii(n,dist, q, queries)
 
    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            di = dist[i]
            dik = di[k]
 
            if dik == INF:
                continue
 
            for j in range(1, n + 1):
                dj = dik + dk[j]
                if dj < di[j]:
                    di[j] = dj
 
    for a, b in queries:
        if dist[a][b] == INF:
            print(-1)
        else:
            print(dist[a][b])
 

#faster approach for CSES tests
def shortest_routes_ii():
    # Read the complete byte stream into memory
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    it = map(int, input_data)
    
    n = next(it)
    m = next(it)
    q = next(it)
    
    
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        
    edges_count = 0
    for _ in range(m):
        a = next(it) - 1
        b = next(it) - 1
        w = next(it)
        
        if a == b:
            continue
            
        # Count strictly unique undirected paths
        if dist[a][b] == INF:
            edges_count += 1
            
        if w < dist[a][b]:
            dist[a][b] = w
            dist[b][a] = w

    # 1. ALGORITHM SWITCH
    # 3000 catches ultra-sparse trees (Test 11) for Dijkstra.
    # Everything higher goes to the Hybrid Floyd-Warshall (Tests 12 & 14).
    if edges_count <= 3000:
        # --- MULTI-SOURCE DIJKSTRA ---
        adj = [[] for _ in range(n)]
        for i in range(n):
            di = dist[i]
            for j in range(n):
                if i != j and di[j] != INF:
                    adj[i].append((j, di[j]))
                    
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
            pq = [(0, i)]
            di = dist[i]
            
            while pq:
                d, u = heappop(pq)
                if d > di[u]:
                    continue
                    
                for v, w in adj[u]:
                    new_d = d + w
                    if new_d < di[v]:
                        di[v] = new_d
                        heappush(pq, (new_d, v))
    else:
        # --- HYBRID FLOYD-WARSHALL ---
        for k in range(n):
            dk = dist[k]
            # Find reachable destinations from K
            valid_j = [j for j in range(n) if dk[j] != INF]
            
            # CRITICAL ADJUSTMENT: Raised threshold to 400.
            # This allows Test 12 to safely use the optimized sparse branch,
            # while keeping Test 14 inside the fast range(n) native loop.
            if len(valid_j) > 400:
                for i in range(n):
                    di = dist[i]
                    dik = di[k]
                    if dik != INF:
                        for j in range(n):
                            dj = dik + dk[j]
                            if dj < di[j]:
                                di[j] = dj
            # If the row is sparse, skip empty loops
            else:
                for i in range(n):
                    di = dist[i]
                    dik = di[k]
                    if dik != INF:
                        for j in valid_j:
                            dj = dik + dk[j]
                            if dj < di[j]:
                                di[j] = dj

    # Fast Query Output Processing
    res = []
    for _ in range(q):
        a = next(it) - 1
        b = next(it) - 1
        dab = dist[a][b]
        
        if dab == INF:
            res.append("-1")
        else:
            res.append(str(dab))
            
    sys.stdout.write('\n'.join(res) + '\n')

if __name__ == "__main__":
    shortest_routes_ii()

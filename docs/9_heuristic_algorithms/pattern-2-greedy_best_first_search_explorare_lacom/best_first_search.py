from heapq import heappush, heappop

# Time Complexity: O(V * log V)
# Space Complexity: O(V + E)
def best_first_search(n: int, edges: list[list[int]], src: int, target: int) -> list[int]:
    # Build adjacency list: adj[u] = [(v, w), ...]
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    visited = [False] * n
    q = []
    
    heappush(q, (0, src))
    visited[src] = True
    path = []
    
    while q:
        _, u = heappop(q)
        path.append(u)
        
        if u == target:
            break
            
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                heappush(q, (w, v))
                
    return path

n = 14
edges = [
    [0, 1, 3], [0, 2, 6], [0, 3, 5],
    [1, 4, 9], [1, 5, 8], [2, 6, 12],
    [2, 7, 14], [3, 8, 7], [8, 9, 5],
    [8, 10, 6], [9, 11, 1], [9, 12, 10],
    [9, 13, 2]
]

path = best_first_search(n, edges, 0, 9)
print(*path)

'''
HEURISTIC SEARCH ANALYSIS (Greedy Best-First Search)

A) Heuristic Approach:
   Instead of exploring level by level (like standard BFS) or calculating the 
   total accumulated cost from the source (like Dijkstra), Greedy Best-First 
   Search uses a Priority Queue to always expand the v with the lowest 
   immediate cost (the heuristic).

B) The "Greedy" Nature:
   The algorithm is greedy because it makes the locally optimal choice at each 
   step, hoping it leads to a global optimum. However, because it ignores the 
   historical cost, it can easily be led down a long, expensive path just because 
   the first step looked cheap. It is fast, but rarely optimal.
'''
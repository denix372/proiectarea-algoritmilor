#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, n, adj):
        disc = [-1] * n
        low = [-1] * n
        timer = 0
        ap = set()
        
        def dfs(u, p):
            nonlocal timer
            disc[u] = low[u] = timer
            timer += 1
            children = 0
            
            for v in adj[u]:
                if v == p:
                    continue
            
                if disc[v] == -1:
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    
                    if p != -1 and low[v] >= disc[u]:
                        ap.add(u)
                else:
                    low[u] = min(low[u], disc[v])
            if p == -1 and children > 1:
                ap.add(u)
            
            
        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)
                
        return sorted(ap) if ap else [-1]
            
V = 5
edges = [[0, 1], [1, 4], [2, 3], [2, 4], [3, 4]]
adj = [[] for _ in range(V)]    
for edge in edges:
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])
ans = Solution().articulationPoints(V, adj)

for u in ans:
    print(u, end=' ')
print()

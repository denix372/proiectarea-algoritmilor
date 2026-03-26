import sys
sys.setrecursionlimit(10**7)
class Solution:
    def isBridge(self, n, edges, c, d):
        adj =[[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # code here 
        disc = [-1] * n
        low = [-1] * n
        timer = 0
        found = False
        
        def dfs(u, p):
            nonlocal timer, found
            disc[u] = low[u] = timer
            timer += 1
            
            for v in adj[u]:
                if v == p:
                    continue
                
                if disc[v] == -1: #tree edge
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    
                    if low[v] > disc[u]: #brigde
                         if (u == c and v == d) or (u == d and v == c):
                            found = True
                    
                else:
                    low[u] = min(low[u], disc[v])
        
        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)
        return found


V = 4
edges = [[0, 1], [1, 2], [2, 3]] 
c, d = 1, 2  
print(Solution().isBridge(V, edges, c, d))
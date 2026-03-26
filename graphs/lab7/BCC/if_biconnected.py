#User function Template for python3

class Solution:
    def biGraph(self, arr, n, e):
        # code here 
        adj = [[] for _ in range(n)]
        for i in range(0, 2*e, 2):
            u = arr[i]
            v = arr[i+1]
            adj[u].append(v)
            adj[v].append(u)
        disc = [-1] * n
        low = [-1] * n
        timer = 0
        stack = []
        bcc_count = 0
        visited_count = 0
        
        def dfs(u, p):
            nonlocal timer, bcc_count, visited_count
            disc[u] = low[u] = timer
            timer += 1
            visited_count += 1
            for v in adj[u]:
                if v == p:
                    continue
            
                if disc[v] == -1: #tree-edge
                    stack.append((u, v))
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
    
                    if low[v] >= disc[u]: #BCC
                        bcc_count += 1
                        while stack and stack[-1] != (u, v):
                            stack.pop()
                        stack.pop()
                    
                elif disc[v] < disc[u]: # back-edge
                    stack.append((u, v))
                    low[u] = min(low[u], disc[v])
                    
        dfs(0, -1)
        
        if visited_count != n:
            return 0
        
        if bcc_count > 1:
            return 0
        
        return 1
        
n = 2
e = 1
arr = [0, 1]
print(Solution().biGraph(arr, n, e))
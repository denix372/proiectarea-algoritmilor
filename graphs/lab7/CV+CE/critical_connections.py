import collections
class Solution(object):
    def criticalConnections(self, n, connections):
        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)

        disc = [-1] * n
        low = [-1] * n
        timer = 0
        bridges = []
        
        def dfs(u, p):
            nonlocal timer
            disc[u] = low[u] = timer
            timer += 1

            for v in adj[u]:
                if v == p:
                    continue

                if disc[v] == -1: # tree edge
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]: #bridge, edge is critical
                        bridges.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])
        dfs(0, -1)
        return bridges


n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
sol = Solution()
print(sol.criticalConnections(n, connections))
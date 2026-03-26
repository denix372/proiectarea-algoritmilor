class Solution:
    def spanningTree(self, n: int, edges: list[list[int]]) -> int:
        
        def find(x):
            if parent[x] != x: 
                parent[x] = find(parent[x]) #path compression
            return parent[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)
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

        parent = list(range(n))
        rank = [0] * n
        cnt = 0
        cost = 0

        edges.sort(key = lambda x : x[2])

        for u, v, w in edges:
            if union(u, v):
                cost += w
                cnt += 1
                if cnt == n - 1:
                    break
        return cost

n = 3
E = 3
Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
print(Solution().spanningTree(n, Edges))
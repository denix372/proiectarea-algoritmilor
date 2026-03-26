from typing  import List
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        new_edges = []
        for i, (u, v, w) in enumerate(edges):
            new_edges.append([u, v, w, i])
        new_edges.sort(key = lambda x : x[2])
    
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        def union(parent, rank, a, b):
            ra = find(parent, a)
            rb = find(parent, b)
            if ra == rb:
                return False
            if rank[ra] > rank[rb]:
                parent[rb] =ra
            elif rank[rb] < rank[ra]:
                parent[ra] =rb
            else:
                parent[ra] = rb
                rank[ra] += 1
            return True

        def kruskal(skip_edge = -1, force_edge = -1):
            parent = list(range(n))
            rank = [0] * n
            cost = 0
            edges_used = 0

            if force_edge != -1:
                u, v, w, _ = new_edges[force_edge]
                union(parent, rank, u, v)
                cost += w
                edges_used += 1

            for i, (u, v, w, _) in enumerate(new_edges):
                if i == skip_edge:
                    continue
                if union(parent, rank, u, v):
                    cost += w
                    edges_used += 1
                if edges_used == n - 1:
                    break
            return cost if edges_used == n - 1 else float("inf")

        base_cost = kruskal()
        critical = []
        pseudo = []
        for i in range(len(new_edges)):
            if kruskal(skip_edge = i) > base_cost:
                critical.append(new_edges[i][3])
            elif kruskal(force_edge= i) == base_cost:
                pseudo.append(new_edges[i][3])
        return [critical, pseudo]
    
n = 5
edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
print(Solution().findCriticalAndPseudoCriticalEdges(n, edges))
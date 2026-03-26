import random

class KargersAlgorithm:
    def __init__(self, vertices: int, edges: list[tuple[int, int]]):
        self.V = vertices
        self.edges = edges

    def min_cut(self) -> int:
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                # Union by rank for O(a(V)) efficiency
                if rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                elif rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        # We start with V isolated components
        components = self.V

        # Keep contracting edges until only 2 components remain
        while components > 2:
            # Pick a random edge from the graph
            u, v = random.choice(self.edges)

            root_u = find(u)
            root_v = find(v)

            # If they belong to the same component, it's a self-loop. Ignore.
            if root_u == root_v:
                continue

            # Contract the edge (merge the components)
            union(root_u, root_v)
            components -= 1

        # Count the number of edges crossing the final two components
        cut_edges = 0
        for u, v in self.edges:
            if find(u) != find(v):
                cut_edges += 1

        return cut_edges

# --- DRIVER CODE (EXAMPLE USAGE) ---
# Constructing a simple "bowtie" graph: 
# 0-1 and 2-3 are strongly connected. Only one edge connects the two halves (1-2).
# The minimum cut should clearly be 1.
V = 4
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]

karger = KargersAlgorithm(V, edges)
print("Minimum cut found by Karger's algorithm:", karger.min_cut())

'''
PROBABILISTIC ANALYSIS & ALGORITHM PROOF (Karger's Min-Cut / Monte Carlo)

A) Core Algorithm Idea:
   The algorithm relies on random edge contraction. At each step, it chooses a 
   uniform random edge and merges its endpoints. It stops when exactly 2 
   vertices (super-nodes) remain. The edges between them form a cut.

B) Classification: Monte Carlo Algorithm
   The algorithm runs in polynomial time but may not always return the optimal 
   (minimum) cut. However, by running it multiple times, we can achieve high 
   probability of success.

C) Mathematical Complexity & Probability of Success:
   Let 'k' be the size of the true minimum cut.
   This means every vertex in the graph must have a degree of at least 'k'.
   Therefore, the total number of edges E in the graph must be at least (k * V) / 2.
   
   Step 1: Probability of picking an edge from the min-cut is:
   P(picking cut edge) = k / E <= k / (kV / 2) = 2 / V.
   Therefore, the probability of NOT ruining the cut (keeping the min-cut intact) is:
   P(success at step 1) >= 1 - (2 / V) = (V - 2) / V.

   Step 2: We contract an edge. Now the graph has V - 1 vertices.
   P(success at step 2) >= 1 - (2 / (V - 1)) = (V - 3) / (V - 1).

   Continuing this until only 2 vertices remain, the total probability of success is 
   the product of the probabilities at each step (telescoping product):
   P(finding min cut) >= [(V - 2) / V] * [(V - 3) / (V - 1)] * [(V - 4) / (V - 2)] ... * [2 / 4] * [1 / 3]
   
   Most terms cancel out, leaving exactly:
   P(finding min cut) >= 2 / (V * (V - 1))
   
   This means a single run has a success probability of Ω(1/V^2).
   While this seems low, running the algorithm O(V^2 * log V) times guarantees 
   a high probability (approaching 1) of finding the absolute minimum cut.

D) Time Complexity:
   - A single run takes O(E) time using Union-Find.
   - To achieve high probability, we run it O(V^2 * log V) times.
   - Total Time Complexity: O(E * V^2 * log V).
   - Space Complexity: O(V + E) for storing edges and Union-Find arrays.
'''
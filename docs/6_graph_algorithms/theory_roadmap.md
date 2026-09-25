# 📖 Theory Roadmap: Graph Algorithms

> 🔗 **[← Back to Problem List](./readme.md)**
>
> Graph algorithms are the backbone of network analysis, pathfinding, and scheduling. This roadmap covers everything from basic traversal to flows and advanced structures.

---

## 🔑 Graph Representations

| Representation | Space | Edge Lookup | Best For |
|----------------|-------|-------------|----------|
| Adjacency List | O(V+E) | O(degree) | Sparse graphs |
| Adjacency Matrix | O(V²) | O(1) | Dense graphs, Floyd-Warshall |
| Edge List | O(E) | O(E) | Kruskal's MST |

---

## SECTION 1: BFS, DFS & Topological Sort

---

### PATTERN 1 — Simple BFS / DFS & Traversal

#### 🧠 Recognize It When…
- "Is there a path?", "find connected components", "flood fill", "count islands."
- Grid-based connectivity problems.

#### 💡 BFS (Shortest Path in Unweighted Graph)

```
from collections import deque
queue = deque([start]); visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

#### 💡 DFS (Recursive)

```
visited = set()
function dfs(node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)
```

| | BFS | DFS |
|--|--|--|
| Time | O(V + E) | O(V + E) |
| Space | O(V) | O(V) stack |
| Shortest path? | ✅ Yes (unweighted) | ❌ No |

---

### PATTERN 2 — Degree Counting & Star Graphs

#### 🧠 Recognize It When…
- "Find the center of a star", "find the town judge."
- Count in-degree and out-degree of each node.

#### 💡 Core Intuition
The "judge" has `in_degree = n-1` and `out_degree = 0`. Track both.

```
in_deg = [0] * (n+1); out_deg = [0] * (n+1)
for a, b in trust:
    out_deg[a] += 1
    in_deg[b] += 1
for i in range(1, n+1):
    if in_deg[i] == n-1 and out_deg[i] == 0:
        return i
```

---

### PATTERN 3 — Topological Sort (Kahn's / DFS)

#### 🧠 Recognize It When…
- DAG with dependencies: "can you complete all courses?", "find valid ordering."
- "Find eventual safe states."

#### 💡 Kahn's Algorithm (BFS-based)

```
in_degree = [0] * n
for course, prereq in prerequisites:
    adj[prereq].append(course)
    in_degree[course] += 1

queue = deque([i for i in range(n) if in_degree[i] == 0])
order = []
while queue:
    node = queue.popleft()
    order.append(node)
    for neighbor in adj[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

return order if len(order) == n else []  # [] = cycle detected
```

#### 💡 DFS-based Topological Sort

```
WHITE, GRAY, BLACK = 0, 1, 2
color = [WHITE] * n; order = []
def dfs(u):
    color[u] = GRAY
    for v in adj[u]:
        if color[v] == GRAY: return False  # cycle!
        if color[v] == WHITE:
            if not dfs(v): return False
    color[u] = BLACK; order.append(u)
    return True
```

| | Complexity |
|--|--|
| Time | O(V + E) |
| Space | O(V) |

---

## SECTION 2: Connected Components, SCC, Bridges

---

### PATTERN 1 — Connected Components (CC)

#### 🧠 Recognize It When…
- "Number of islands", "count distinct groups", "union-find."

#### 💡 BFS/DFS per Component

```
count = 0
for node in range(n):
    if not visited[node]:
        bfs_or_dfs(node)  # mark entire component
        count += 1
```

---

### PATTERN 2 — Strongly Connected Components (SCC)

#### 🧠 Recognize It When…
- Directed graph: "nodes that can reach each other."
- Condensation DAG for optimization.

#### 💡 Kosaraju's Algorithm

1. DFS on original graph → finish-time order (stack).
2. Transpose (reverse) the graph.
3. DFS on transposed graph in reverse finish-time order → each DFS tree is one SCC.

```
# Step 1: fill stack by finish time
def dfs1(v):
    visited.add(v)
    for u in graph[v]:
        if u not in visited: dfs1(u)
    stack.append(v)

# Step 2: DFS on transposed graph
def dfs2(v, component):
    visited.add(v); component.append(v)
    for u in transposed[v]:
        if u not in visited: dfs2(u, component)
```

| | Complexity |
|--|--|
| Time | O(V + E) |
| Space | O(V + E) |

---

### PATTERN 3 — Bridges & Articulation Points (Tarjan)

#### 🧠 Recognize It When…
- "Critical connections" — removing which edges disconnects the graph?
- "Articulation points" — which nodes, if removed, disconnect the graph?

#### 💡 Tarjan's Bridge-Finding Algorithm

Use DFS with `disc` (discovery time) and `low` (lowest reachable disc).  
An edge `(u, v)` is a **bridge** if `low[v] > disc[u]`.

```
timer = 0
disc = [-1] * n; low = [-1] * n
def dfs(u, parent):
    global timer
    disc[u] = low[u] = timer; timer += 1
    for v in adj[u]:
        if disc[v] == -1:
            dfs(v, u)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                bridges.append((u, v))    # bridge!
        elif v != parent:
            low[u] = min(low[u], disc[v])
```

---

## SECTION 3: Shortest Path I — Dijkstra & Bellman-Ford

---

### PATTERN 1 — Dijkstra's Algorithm

#### 🧠 Recognize It When…
- Weighted graph, **non-negative** edge weights.
- Single-source shortest path: "minimum time/cost to reach each node."

#### 💡 Pseudocode

```
dist = [inf] * n; dist[src] = 0
heap = [(0, src)]
while heap:
    d, u = heappop(heap)
    if d > dist[u]: continue    # stale entry
    for (v, w) in adj[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heappush(heap, (dist[v], v))
```

| | Complexity |
|--|--|
| Time | O((V + E) log V) |
| Space | O(V + E) |

> ⚠️ **Cannot handle negative weights.** Use Bellman-Ford instead.

---

### PATTERN 2 — Bellman-Ford & Negative Cycles

#### 🧠 Recognize It When…
- Graph has **negative edge weights**.
- Detect **negative cycles** (e.g., arbitrage opportunities).
- Single-source shortest path with at most K hops.

#### 💡 Pseudocode

```
dist = [inf] * n; dist[src] = 0
for _ in range(n - 1):       # n-1 relaxation rounds
    for (u, v, w) in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

# Check for negative cycles (n-th round still relaxes)
for (u, v, w) in edges:
    if dist[u] + w < dist[v]:
        return "Negative cycle detected"
```

| | Complexity |
|--|--|
| Time | O(V × E) |
| Space | O(V) |

---

### PATTERN 3 — 0-1 BFS & Multi-Source BFS

#### 🧠 Recognize It When…
- Edges have weight 0 or 1 only (use deque, not heap).
- Multiple starting sources simultaneously (e.g., rotting oranges).

#### 💡 0-1 BFS (Deque)

```
dist = [inf] * n; dist[src] = 0
deque = [src]
while deque:
    u = deque.popleft()
    for (v, w) in adj[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            if w == 0: deque.appendleft(v)   # 0-weight → front
            else:      deque.append(v)        # 1-weight → back
```

| | Complexity |
|--|--|
| Time | O(V + E) |
| Space | O(V) |

---

## SECTION 4: Shortest Path II — Floyd-Warshall & Johnson's

---

### PATTERN 1 — Floyd-Warshall (All-Pairs Shortest Path)

#### 🧠 Recognize It When…
- Need shortest paths **between every pair** of nodes.
- Small graph (V ≤ 500 typically).

#### 💡 Pseudocode

```
dist = adjacency_matrix (inf where no edge)
dist[i][i] = 0 for all i

for k in range(n):          # intermediate node
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

| | Complexity |
|--|--|
| Time | O(V³) |
| Space | O(V²) |

---

### PATTERN 2 — Johnson's Algorithm

#### 🧠 Recognize It When…
- Sparse graph with **negative edges** and you need **all-pairs** shortest paths.
- More efficient than V × Bellman-Ford.

#### 💡 Core Idea
1. Add a virtual node `q` with 0-weight edges to all other nodes.
2. Run Bellman-Ford from `q` to get `h[v]` (potential function).
3. Reweight all edges: `w'(u,v) = w(u,v) + h[u] - h[v]` (all non-negative now).
4. Run Dijkstra from every node using reweighted edges.

| | Complexity |
|--|--|
| Time | O(V·E + V² log V) |
| Space | O(V + E) |

---

## SECTION 5: Minimum Spanning Trees (MST) & DSU

---

### PATTERN 1 — Kruskal's + Disjoint Set Union (DSU)

#### 🧠 Recognize It When…
- "Minimum cost to connect all nodes", "minimum spanning tree."
- Offline connectivity queries.

#### 💡 DSU with Path Compression + Union by Rank

```
parent = list(range(n)); rank = [0] * n

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])  # path compression
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py: return False          # already connected
    if rank[px] < rank[py]: px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]: rank[px] += 1
    return True
```

| Operation | Amortized Complexity |
|--|--|
| find / union | O(α(n)) ≈ O(1) |
| Kruskal's total | O(E log E) |

---

### PATTERN 2 — Prim's Algorithm

#### 🧠 Recognize It When…
- Dense graph where Prim's is more efficient than Kruskal's.
- MST growing from a single node.

#### 💡 Pseudocode (Min-Heap)

```
visited = {0}; heap = [(0, 0)]  # (cost, node)
total_cost = 0
while heap and len(visited) < n:
    cost, u = heappop(heap)
    if u in visited: continue
    visited.add(u); total_cost += cost
    for v, w in adj[u]:
        if v not in visited:
            heappush(heap, (w, v))
```

| | Complexity |
|--|--|
| Prim's (heap) | O((V + E) log V) |

---

## SECTION 6: Network Flow

---

### PATTERN 1 — Max Flow (Ford-Fulkerson / Edmonds-Karp)

#### 🧠 Recognize It When…
- "Maximum flow from source to sink", "minimum cut."
- Bipartite matching, network capacity problems.

#### 💡 Core Concept — Augmenting Paths

Repeatedly find a path from source `s` to sink `t` with remaining capacity > 0. Push flow along it. Repeat until no augmenting path exists.

```
while path = BFS(s, t, residual_graph):    # Edmonds-Karp uses BFS
    bottleneck = min(residual[u][v] for (u,v) in path)
    for (u, v) in path:
        residual[u][v] -= bottleneck
        residual[v][u] += bottleneck      # reverse edge
    max_flow += bottleneck
```

> 🔑 **Max-Flow Min-Cut Theorem**: The maximum flow equals the capacity of the minimum cut (minimum total capacity to disconnect s from t).

| | Complexity |
|--|--|
| Ford-Fulkerson | O(E × max_flow) |
| Edmonds-Karp (BFS) | O(V × E²) |

---

### PATTERN 2 — Bipartite Matching

#### 🧠 Recognize It When…
- Two disjoint sets, match items between them.
- "Assign workers to jobs", "matching students to projects."

#### 💡 Reduction to Max Flow

Add super-source → all nodes in set A (capacity 1), all nodes in set B → super-sink (capacity 1), and edges A→B (capacity 1). Run max flow.

```
# Or use Hopcroft-Karp for O(E √V)
match_l = [-1] * m; match_r = [-1] * n

def dfs(u, visited):
    for v in adj[u]:
        if v not in visited:
            visited.add(v)
            if match_r[v] == -1 or dfs(match_r[v], visited):
                match_l[u] = v; match_r[v] = u
                return True
    return False
```

---

## SECTION 7: Advanced / Rare Topics

---

### PATTERN 1 — Eulerian Circuits & Paths

#### 🧠 Recognize It When…
- "Reconstruct an itinerary", "traverse all edges exactly once."

#### 💡 Conditions

- **Euler Circuit**: All vertices have **even degree** (undirected) or equal in/out degree (directed).
- **Euler Path**: Exactly 2 vertices with odd degree (undirected) or exactly one with `out-in = 1` and one with `in-out = 1` (directed).

#### 💡 Hierholzer's Algorithm

```
function eulerCircuit(start, graph):
    stack = [start]; path = []
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            stack.append(u)
        else:
            path.append(stack.pop())
    return reversed(path)
```

| | Complexity |
|--|--|
| Time | O(E) |
| Space | O(E) |

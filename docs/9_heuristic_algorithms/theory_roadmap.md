# 📖 Theory Roadmap: Heuristic Algorithms

> 🔗 **[← Back to Problem List](./readme.md)**
>
> **Heuristic (Informed) Search** uses domain knowledge to guide the search toward the goal faster than blind search (BFS/DFS). The quality of the heuristic determines the quality of the solution found.

---

## 🔑 Core Framework: f(n) = g(n) + h(n)

| Symbol | Meaning |
|--------|---------|
| `g(n)` | Exact cost from **start → current node** |
| `h(n)` | **Heuristic estimate** of cost from current node → goal |
| `f(n)` | Total estimated path cost through node `n` |

**Heuristic Quality:**

| Property | Condition | Guarantee |
|----------|-----------|-----------|
| **Admissible** | `h(n) ≤ h*(n)` (never overestimates) | A* finds optimal path |
| **Consistent (Monotone)** | `h(n) ≤ c(n,n') + h(n')` for every edge | No node revisited in A*, implies admissible |

> 🎯 **Dominance**: If `h₁(n) ≥ h₂(n)` for all `n` (and both admissible), then `h₁` **dominates** `h₂` and A* with `h₁` expands fewer nodes.

---

## PATTERN 1 — Hill Climbing & Simulated Annealing

---

### 🧠 Recognize It When…
- Optimization problem with no guarantee of global optimum needed.
- Only the **current state** and its **neighbors** are considered.
- Cannot afford to store the entire search frontier.

---

### 💡 Hill Climbing

Always move to the neighbor with the best evaluation. Simple but **incomplete** (gets stuck in local optima).

```
current = initial_state()
while True:
    neighbors = get_neighbors(current)
    best_neighbor = max(neighbors, key=evaluate)
    if evaluate(best_neighbor) <= evaluate(current):
        break    # local maximum — stop
    current = best_neighbor
return current
```

**Variants**:
- **Steepest Ascent**: Check all neighbors, pick the best.
- **First Choice**: Pick the first neighbor better than current.
- **Random Restart**: Run multiple times from random starts, take the best.

---

### 💡 Simulated Annealing

Accept worse moves with probability `P = e^(-ΔE/T)` where `T` is the "temperature" that decreases over time. This allows **escaping local optima** early in the search.

```
current = initial_state()
T = T_initial
while T > T_min:
    neighbor = random_neighbor(current)
    delta = evaluate(neighbor) - evaluate(current)
    if delta > 0 or random() < exp(delta / T):
        current = neighbor    # accept move (even if worse!)
    T = T * cooling_rate      # cool down (e.g., cooling_rate = 0.995)
return current
```

> 🔑 **Analogy**: Like annealing metal — high temperature = many random moves (explore broadly), low temperature = settle into local optimum.

| Algorithm | Complete | Optimal | Time |
|-----------|----------|---------|------|
| Hill Climbing | ❌ | ❌ | O(∞) potential |
| Simulated Annealing | ✅ (in theory) | ✅ (in theory) | Depends on schedule |

---

## PATTERN 2 — Greedy Best-First Search

---

### 🧠 Recognize It When…
- Find a path quickly, optimality not required.
- A good heuristic exists that estimates closeness to the goal.

---

### 💡 Core Intuition

Expand the node that **looks** closest to the goal (minimizes `h(n)`), ignoring the cost to reach it (`g(n)`).

```
open_list = PriorityQueue(key=h)    # min-heap by h(n)
open_list.push(start)
closed_list = set()

while open_list:
    current = open_list.pop()   # node with min h(n)
    if current == goal: return path
    closed_list.add(current)
    for neighbor in get_neighbors(current):
        if neighbor not in closed_list:
            open_list.push(neighbor)
```

| | Property |
|--|--|
| Complete | ❌ Can loop (need closed list) |
| Optimal | ❌ Ignores actual cost g(n) |
| Time / Space | O(b^m) — m = max depth |

> ⚡ **Faster than A\*** in practice on many problems, but can lead to suboptimal solutions.

---

## PATTERN 3 — Beam Search

---

### 🧠 Recognize It When…
- Memory-constrained environment (can't store the entire frontier).
- NLP sequence generation, large state spaces.

---

### 💡 Core Intuition

At each level, keep only the **top B candidates** (beam width). Discard the rest. Trade-off: speed vs. completeness.

```
beam = [start]    # initial beam of width 1
while beam not all terminal:
    candidates = []
    for node in beam:
        for child in expand(node):
            candidates.append(child)
    # Sort by heuristic and keep top B
    beam = sorted(candidates, key=h)[:B]
return best(beam)
```

| Beam Width | Behavior |
|------------|----------|
| B = 1 | Hill Climbing |
| B = ∞ | Best-First Search (BFS) |
| B = K | Trade-off: quality vs. memory |

> ⚠️ Beam Search is **neither complete nor optimal** — it may discard the optimal path.

---

## PATTERN 4 — Grid Pathfinding: A* Search

---

### 🧠 Recognize It When…
- Find the **shortest path** in a grid with obstacles.
- A good admissible heuristic is available.
- BFS is too slow (large grid, high obstacle density).

---

### 💡 A* Algorithm

Combine Dijkstra's optimality (`g(n)`) with heuristic speed (`h(n)`).

```
open_set = PriorityQueue(key=f)    # ordered by f(n) = g(n) + h(n)
open_set.push((f(start), start))
g = defaultdict(lambda: inf); g[start] = 0
came_from = {}

while open_set:
    _, current = open_set.pop()
    if current == goal: return reconstruct_path(came_from, current)
    for neighbor, cost in get_neighbors(current):
        new_g = g[current] + cost
        if new_g < g[neighbor]:
            came_from[neighbor] = current
            g[neighbor] = new_g
            f_val = new_g + h(neighbor)
            open_set.push((f_val, neighbor))
return None   # no path
```

---

### 💡 Common Heuristics for Grids

| Movement Type | Heuristic | Formula |
|---------------|-----------|---------|
| 4-directional | **Manhattan Distance** | `|dx| + |dy|` |
| 8-directional | **Chebyshev Distance** | `max(|dx|, |dy|)` |
| Any direction | **Euclidean Distance** | `√(dx² + dy²)` |

> 🔑 **Manhattan Distance** is admissible for 4-directional movement because it never overestimates the actual path length.

| | A* | BFS |
|--|--|--|
| Optimal | ✅ (admissible h) | ✅ (unweighted) |
| Time | O(b^d) best case | O(b^d) |
| In practice | Much faster with good h | Explores all directions |

---

## PATTERN 5 — State-Space Search & Heuristic Dominance

---

### 🧠 Recognize It When…
- Complex puzzle states (8-puzzle, 15-puzzle).
- Multiple heuristics available — choosing the **dominant** one reduces nodes expanded.

---

### 💡 8-Puzzle Example

**State**: 3×3 grid with tiles 1-8 and one blank.  
**Goal**: Reach the sorted configuration.

Two heuristics (both admissible):
1. **Misplaced Tiles** `h₁`: Count tiles not in goal position.
2. **Manhattan Distance** `h₂`: Sum of Manhattan distances of each tile to its goal position.

**Dominance**: `h₂(n) ≥ h₁(n)` for all `n` → `h₂` dominates `h₁` → A* with `h₂` expands **fewer nodes**.

```
def h_manhattan(state, goal):
    total = 0
    for tile in range(1, 9):
        r1, c1 = find(state, tile)
        r2, c2 = find(goal, tile)
        total += abs(r1-r2) + abs(c1-c2)
    return total

def h_misplaced(state, goal):
    return sum(1 for i in range(9) if state[i] != goal[i] and state[i] != 0)
```

> 🔑 **Rule**: Always use the most informed (largest) admissible heuristic you can compute efficiently.

---

## PATTERN 6 — Warnsdorff's Heuristic (Knight's Tour)

---

### 🧠 Recognize It When…
- Knight's Tour problem: visit every cell of an N×N board exactly once.
- Naive backtracking is too slow for large boards.

---

### 💡 Warnsdorff's Rule

> Always move to the adjacent unvisited square that has the **fewest onward moves**.

This is a domain-specific heuristic that guides the knight away from "dead ends" early, dramatically reducing backtracking.

```
def warnsdorff(board, r, c):
    moves = []
    for dr, dc in KNIGHT_MOVES:
        nr, nc = r + dr, c + dc
        if is_valid(board, nr, nc):
            # Count onward moves from (nr, nc)
            onward = count_valid_moves(board, nr, nc)
            moves.append((onward, nr, nc))
    # Sort by fewest onward moves (ties broken arbitrarily)
    moves.sort()
    return moves[0][1], moves[0][2] if moves else None

# Main loop
for step in range(n*n - 1):
    next_r, next_c = warnsdorff(board, r, c)
    board[next_r][next_c] = step + 1
    r, c = next_r, next_c
```

| | Warnsdorff | Naive Backtracking |
|--|--|--|
| Time (n=8) | O(n²) | O(n²)! worst |
| Solution found | Nearly always on 1st try | May require deep search |
| Optimal? | ❌ (heuristic) | ✅ (finds all solutions) |

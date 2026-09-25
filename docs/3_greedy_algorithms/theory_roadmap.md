# 📖 Theory Roadmap: Greedy Algorithms

> 🔗 **[← Back to Problem List](./readme.md)**
>
> A **greedy algorithm** makes the locally optimal choice at each step with the hope of finding a global optimum. It works when the problem exhibits the **Greedy Choice Property** and **Optimal Substructure**.

---

## 🟢 When Does Greedy Work?

| Property | Meaning |
|----------|---------|
| **Greedy Choice Property** | A global optimum can always be reached by making a locally optimal (greedy) choice first |
| **Optimal Substructure** | The optimal solution to the problem contains optimal solutions to subproblems |

> ⚠️ **If both properties hold → Greedy is correct.**  
> If not, you likely need **Dynamic Programming**.

---

## PATTERN 1 — Foundations & Simple Selection

---

### 🧠 Recognize It When…
- Simple scan through elements making a binary (include/skip) decision.
- "Maximize sum by keeping positives / flipping negatives."
- "Assign cookies to children greedily."

---

### 💡 Core Intuition
Sort by the relevant criterion, then greedily pick from the best candidates. No backtracking needed.

```
# Maximize sum of subsequence (only positive)
total = 0
for x in arr:
    if x > 0:
        total += x

# Assign cookies: sort both, give smallest sufficient cookie to each child
sort(children); sort(cookies)
child = 0
for cookie in cookies:
    if cookie >= children[child]:
        child++
return child   # number of satisfied children
```

| | Complexity |
|--|--|
| Time | O(n log n) — dominated by sorting |
| Space | O(1) |

---

## PATTERN 2 — Intervals & Scheduling

---

### 🧠 Recognize It When…
- Input is a list of `[start, end]` intervals/events.
- "Maximum non-overlapping activities", "minimum arrows to burst balloons."

---

### 💡 Core Intuition — Activity Selection (Sort by End Time)

> 🔑 **Key Rule**: Always sort by **end time** and greedily pick the activity that ends earliest — this leaves the maximum time for future activities.

```
# Maximum number of non-overlapping intervals
sort intervals by end time
last_end = -infinity; count = 0
for [start, end] in intervals:
    if start >= last_end:   # compatible with last chosen
        count++
        last_end = end
```

> **Minimum intervals to remove** = `total - max non-overlapping` (same logic, different view).

```
# Merge Intervals (sort by start time instead)
sort by start
merged = [intervals[0]]
for [s, e] in intervals[1:]:
    if s <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], e)
    else:
        merged.append([s, e])
```

| | Complexity |
|--|--|
| Time | O(n log n) |
| Space | O(1) or O(n) for merge output |

---

## PATTERN 3 — Resource Optimization: Knapsack & Refills

---

### 🧠 Recognize It When…
- Maximize value within a weight/capacity limit (fractions allowed).
- "Go as far as possible on one tank", "minimum refueling stops."

---

### 💡 Fractional Knapsack

Sort items by **value/weight ratio** (descending). Take as much of the highest-ratio item as possible, then move to the next.

```
sort items by (value / weight) descending
total_value = 0; remaining_capacity = W
for item in items:
    if remaining_capacity >= item.weight:
        total_value += item.value
        remaining_capacity -= item.weight
    else:
        total_value += item.value * (remaining_capacity / item.weight)
        break
```

---

### 💡 Car Refueling (Minimum Stops)

Greedy: travel as far as possible. When you run out of fuel, refuel at the **last passed station** with the most fuel.

```
# Use a max-heap of passed stations' fuel amounts
heap = []; stops = 0; fuel = tank
for station in stations + [(destination, 0)]:
    fuel -= station.position - prev_position
    while fuel < 0:
        if heap is empty: return -1   # impossible
        fuel += heappop_max(heap)
        stops++
    heappush_max(heap, station.fuel)
```

| | Complexity |
|--|--|
| Fractional Knapsack | O(n log n) |
| Car Refueling | O(n log n) — heap operations |

---

## PATTERN 4 — Deadlines & Profits: Job Sequencing

---

### 🧠 Recognize It When…
- Jobs have **deadlines** and **profits**; at most one job per time slot.
- "Course Schedule III", "maximize number of courses/tasks completed."

---

### 💡 Core Intuition

Sort jobs by **profit** descending (or deadline ascending). Greedily accept the most profitable job and assign it to the **latest available slot** before its deadline. If no slot is available but a lower-profit job is in the schedule, consider swapping.

```
# Classic Job Sequencing
sort jobs by profit descending
slot = [False] * (max_deadline + 1)
result = []
for job in jobs:
    # Find the latest free slot before deadline
    for t in range(job.deadline, 0, -1):
        if not slot[t]:
            slot[t] = True
            result.append(job)
            break
```

---

### 💡 Course Schedule III (Greedy + Max-Heap)

Sort courses by deadline. Greedily take each course; if taking it would exceed the deadline, check if replacing the longest previously taken course saves time.

```
sort courses by deadline
heap = []   # max-heap of durations taken so far
time = 0
for duration, deadline in courses:
    heappush_max(heap, duration)
    time += duration
    if time > deadline:
        time -= heappop_max(heap)   # drop the longest course
return len(heap)
```

| | Complexity |
|--|--|
| Time | O(n log n) |
| Space | O(n) |

---

## PATTERN 5 — Number & String Construction

---

### 🧠 Recognize It When…
- Build the **lexicographically smallest / largest** result digit by digit.
- "Remove K digits", "monotone increasing digits."

---

### 💡 Core Intuition — Monotonic Stack Greedy

To get the smallest number after removing K digits: greedily remove a digit if it is **larger** than the next digit (use a monotonic stack to maintain an increasing sequence).

```
# Remove K Digits → smallest result
stack = []
for digit in number:
    while K > 0 and stack and stack[-1] > digit:
        stack.pop()
        K -= 1
    stack.append(digit)
# Remove any remaining from the end
if K > 0: stack = stack[:-K]
result = ''.join(stack).lstrip('0') or '0'
```

---

### 💡 Smallest Subsequence / Remove Duplicate Letters

Maintain a **monotonic stack** while ensuring each character appears at least once in the result. Use a "last occurrence" map to know when it's safe to skip a character.

```
last = {c: i for i, c in enumerate(s)}
stack = []; seen = set()
for i, c in enumerate(s):
    if c in seen: continue
    while stack and c < stack[-1] and last[stack[-1]] > i:
        seen.discard(stack.pop())
    stack.append(c)
    seen.add(c)
return ''.join(stack)
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(Σ) — alphabet size |

---

## PATTERN 6 — Advanced Greedy: Graphs & Heaps

---

### 🧠 Recognize It When…
- Greedy logic applied to graph problems (MST, shortest paths).
- "Minimum cost to connect", "Huffman encoding."

---

### 💡 Huffman Coding

Build an **optimal prefix-free** binary code. Always merge the two nodes with the **lowest frequency**.

```
heap = [(freq, char) for char, freq in frequencies.items()]
heapify(heap)
while len(heap) > 1:
    f1, n1 = heappop(heap)
    f2, n2 = heappop(heap)
    heappush(heap, (f1 + f2, merge(n1, n2)))
huffman_tree = heap[0]
```

| Code Length | O(n log n) build |
|--|--|
| Time | O(n log n) |
| Space | O(n) |

---

### 💡 Kruskal's MST (Greedy on Edges)

Sort all edges by weight. Add an edge if it doesn't form a cycle (use DSU/Union-Find to track components).

```
sort edges by weight
dsu = DisjointSetUnion(n)
mst_cost = 0; mst_edges = []
for (weight, u, v) in edges:
    if dsu.find(u) ≠ dsu.find(v):
        dsu.union(u, v)
        mst_cost += weight
        mst_edges.append((u, v))
```

| | Complexity |
|--|--|
| Time | O(E log E) |
| Space | O(V) |

---

### 💡 Dijkstra's Algorithm (Greedy on Nodes)

Always visit the **unvisited node with the smallest known distance**. Use a min-heap for efficiency.

```
dist = [inf] * n; dist[src] = 0
heap = [(0, src)]   # (distance, node)
while heap:
    d, u = heappop(heap)
    if d > dist[u]: continue   # stale entry
    for (v, weight) in adj[u]:
        if dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
            heappush(heap, (dist[v], v))
```

| | Complexity |
|--|--|
| Time | O((V + E) log V) |
| Space | O(V + E) |

> ⚠️ **Dijkstra requires non-negative edge weights.** For negative weights, use Bellman-Ford.

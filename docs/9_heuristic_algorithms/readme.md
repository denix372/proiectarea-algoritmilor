---
title: Heuristic Algorithms
---

# 🤖 Heuristic Algorithms & AI Search Roadmap

[📖 Read the Theory Roadmap](./theory_roadmap.md)

**Complexity & Theory Primer:**
Unlike uninformed search (like BFS or IDDFS) which explores blindly, **Informed Search** uses a heuristic function to "guess" the best direction. 
The total estimated cost is usually defined as $f(n) = g(n) + h(n)$, where:
- $g(n)$ is the exact cost from the start node to the current node $n$.
- $h(n)$ is the heuristic estimate of the cost from node $n$ to the goal.

To guarantee that an algorithm like A* finds the **optimal** (shortest) path, the heuristic $h(n)$ must be **admissible** (optimistic). This means it never overestimates the true cost to the goal: $h(n) \le h^*(n)$. A heuristic is even stronger if it is **consistent (monotone)**, meaning $h(n) \le h(n') + c(n, n')$, which automatically makes it admissible.

---

### PATTERN 1: Hill Climbing & Simulated Annealing

*Concept: Irrevocable local search algorithms that only keep track of the current state and its immediate neighbors. They move strictly toward higher/better values and cannot backtrack. They are fast but not complete and not optimal, as they easily get stuck in "local optima".*
- **Hill Climbing:** Always picks the best neighbor.
- **Simulated Annealing:** Probabilistically accepts worse moves early on to escape local maxima, slowly "cooling down" to behave like Hill Climbing.

#### 🔥 Standard
- [N-Queens (Solving via Hill Climbing / Min-Conflicts) — LeetCode 51](https://leetcode.com/problems/n-queens/)
- [Travelling Salesman Problem (Using Simulated Annealing) — GFG](https://www.geeksforgeeks.org/artificial-intelligence/hill-climbing-and-simulated-annealing-for-the-traveling-salesman-problem/)

#### 🧩 Practice
- [Find Peak Element (A basic 1D local maximum search) — LeetCode 162](https://leetcode.com/problems/find-peak-element/)
- [Maximum/Minimum of a mathematical function using Hill Climbing — GFG](https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/)

---

### PATTERN 2: Greedy Best-First Search

*Concept: Expands the node that appears closest to the goal, ignoring the cost taken to get there ($f(n) = h(n)$). It is fast but NOT optimal, and can get stuck in infinite loops if a CLOSED list isn't used to track visited territory.*

#### 🔥 Standard
- [Introduction to Beam Search Algorithm — GFG](https://www.geeksforgeeks.org/beam-search-algorithm-in-ai/)

#### 🧩 Practice
- [Word Ladder (Demonstrating how limiting beam width prunes optimal paths) — LeetCode 127](https://leetcode.com/problems/word-ladder/)
---

### PATTERN 3: Beam Search

*Concept: A memory-optimized variation of Best-First Search that only keeps the top `B` (Beam Width) best nodes in the OPEN list at any level.*

#### 🧩 Practice
- [Word Ladder (Optimizing BFS with a beam width) — LeetCode 127](https://leetcode.com/problems/word-ladder/)
- [Sequence generation in Natural Language Processing (NLP) — GFG Theory](https://www.geeksforgeeks.org/machine-learning/introduction-to-beam-search-algorithm/)

---

### PATTERN 4: Grid Pathfinding Euclidean & Manhattan Distance

*Concept: The crown jewel of pathfinding (A\* Search). Uses $f(n) = g(n) + h(n)$. If the heuristic is admissible, A\* is both **complete** and **optimal**. Applies distance heuristics to navigate 2D grids faster than standard BFS.*

#### 🔥 Standard
- [Shortest Path in Binary Matrix (Perfect for A* with Chebyshev Distance) — LeetCode 1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/)

#### 🧩 Practice
- [Shortest Path in a Grid with Obstacles Elimination (A* in 3D State-Space) — LeetCode 1293](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

---

### PATTERN 5: State-Space Search & Dominance

*Concept: Applying A\* to complex configurations (like board games). If heuristic $h_1$ is strictly greater than (more informed than) $h_2$, $A^*$ using $h_1$ will explore fewer nodes and **dominate** the search.*

#### 🔥 Standard
- [Sliding Puzzle (The classic 8-Puzzle from the university course) — LeetCode 773](https://leetcode.com/problems/sliding-puzzle/)
- *Note on 8-Puzzle Heuristics:* The Manhattan Distance heuristic is more informed (dominates) the Misplaced Tiles heuristic because it provides a closer estimate to the true cost without overestimating.

#### 🌀 Niche
- [Minimum Number of Flips to Convert Binary Matrix to Zero Matrix — LeetCode 1284](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [Cut Off Trees for Golf Event (A* applied to multiple targets) — LeetCode 675](https://leetcode.com/problems/cut-off-trees-for-golf-event/)

---

### PATTERN 6: Warnsdorffs Heuristic

*Concept: A 
domain-specific heuristic designed specifically for the Knight's Tour problem. The rule is to always move to the adjacent unvisited square with the fewest onward moves. This drastically prunes the backtracking tree.*

#### 🔥 Standard
- [Knight's Tour (Warnsdorff's Algorithm) — GFG](https://www.geeksforgeeks.org/warnsdorffs-algorithm-knight-tour-problem/)

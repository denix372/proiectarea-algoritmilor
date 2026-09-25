# 🤖 Heuristic Algorithms & AI Search Roadmap

**Complexity & Theory Primer:**
Unlike uninformed search (like BFS or IDDFS) which explores blindly, **Informed Search** uses a heuristic function to "guess" the best direction. 
The total estimated cost is usually defined as $f(n) = g(n) + h(n)$, where:
* $g(n)$ is the exact cost from the start node to the current node $n$.
* $h(n)$ is the heuristic estimate of the cost from node $n$ to the goal.

To guarantee that an algorithm like A* finds the **optimal** (shortest) path, the heuristic $h(n)$ must be **admissible** (optimistic). This means it never overestimates the true cost to the goal: $h(n) \le h^*(n)$. A heuristic is even stronger if it is **consistent (monotone)**, meaning $h(n) \le h(n') + c(n, n')$, which automatically makes it admissible.

---

## PATTERN: Hill Climbing & Simulated Annealing

[[PATTERN_CARD_HERE]]

*Concept: Irrevocable local search algorithms that only keep track of the current state and its immediate neighbors. They move strictly toward higher/better values and cannot backtrack. They are fast but not complete and not optimal, as they easily get stuck in "local optima".*
* **Hill Climbing:** Always picks the best neighbor.
* **Simulated Annealing:** Probabilistically accepts worse moves early on to escape local maxima, slowly "cooling down" to behave like Hill Climbing.

### 🔥 Standard (AI Theory & Simulation)
- [x] [N-Queens using Hill Climbing- GFG](https://www.geeksforgeeks.org/dsa/n-queen-problem-local-search-using-hill-climbing-with-random-neighbour/)
- [x] [Travelling Salesman Problem (Using Simulated Annealing) - GFG](https://www.geeksforgeeks.org/artificial-intelligence/hill-climbing-and-simulated-annealing-for-the-traveling-salesman-problem/)

### 🧩 Practice (Mathematical Optimization)
- [x] [Find Peak Element - LeetCode 162](./hill_climbing_and_simulated_annealing/find_peak_element.py) — https://leetcode.com/problems/find-peak-element/
- [x] [Maximum/Minimum of a mathematical function using Hill Climbing - GFG](https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/)

---

## PATTERN: Greedy Best-First Search

[[PATTERN_CARD_HERE]]

*Concept: Expands the node that appears closest to the goal, ignoring the cost taken to get there ($f(n) = h(n)$). It is fast but NOT optimal, and can get stuck in infinite loops if a CLOSED list isn't used to track visited territory.It is used when finding ANY path quickly is more important than finding the SHORTEST path*

### 🔥 Standard (AI Theory & Graphs)
- [x]  [Best First Search (Informed Search) - GFG](./greedy_best-first_search/best_first_search.py) — https://www.geeksforgeeks.org/dsa/best-first-search-informed-search/


---

## PATTERN: Beam Search

[[PATTERN_CARD_HERE]]

*Concept: A memory-optimized variation of Best-First Search that only keeps the top B (Beam Width) best nodes in the OPEN list at any level. It sacrifices completeness to save memory.*

### 🔥 Standard (AI Theory)
- [x]   [Introduction to Beam Search Algorithm - GFG](./beam_search/beam_search_algorithm.py) — https://www.geeksforgeeks.org/machine-learning/introduction-to-beam-search-algorithm/

### 🧩 Practice
- [x]  [Word Ladder - LeetCode 127](./beam_search/word_ladder.py) — https://leetcode.com/problems/word-ladder/
---

## PATTERN: Grid Pathfinding (Euclidean & Manhattan Distance)

[[PATTERN_CARD_HERE]]

*Concept: The crown jewel of pathfinding (A* Search). Uses $f(n) = g(n) + h(n)$. If the heuristic is admissible, A* is both **complete** and **optimal**. Applies distance heuristics to navigate 2D grids faster than standard BFS.*

### 🔥 Standard
- [x] [Shortest Path in Binary Matrix - LeetCode 1091](./grid_pathfinding/shortest_path_in_binary_matrix.py) — https://leetcode.com/problems/shortest-path-in-binary-matrix/
### 🧩 Practice
- [x] [Shortest Path in a Grid with Obstacles Elimination - LeetCode 1293](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

---

## PATTERN: State-Space Search & Dominance

[[PATTERN_CARD_HERE]]

*Concept: Applying A* to complex configurations (like board games). If heuristic $h_1$ is strictly greater than (more informed than) $h_2$, $A^*$ using $h_1$ will explore fewer nodes and **dominate** the search.*

### 🔥 Standard
- [x] [Sliding Puzzle - LeetCode 773](./state-space_search_and_dominance/sliding_puzzle.py) — https://leetcode.com/problems/sliding-puzzle/
  *Note on 8-Puzzle Heuristics:* The Manhattan Distance heuristic is more informed (dominates) the Misplaced Tiles heuristic because it provides a closer estimate to the true cost without overestimating.

### 🌀 Niche
- [ ] [Minimum Number of Flips to Convert Binary Matrix to Zero Matrix - LeetCode 1284](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [ ] [Cut Off Trees for Golf Event - LeetCode 675](https://leetcode.com/problems/cut-off-trees-for-golf-event/)

---

## PATTERN: Warnsdorff’s Heuristic

[[PATTERN_CARD_HERE]]

*Concept: A domain-specific heuristic designed specifically for the Knight's Tour problem. The rule is to always move to the adjacent unvisited square with the fewest onward moves. This drastically prunes the backtracking tree.*

### 🔥 Standard
- [x] [Knight's Tour (Warnsdorff's Algorithm) - GFG](https://www.geeksforgeeks.org/warnsdorffs-algorithm-knight-tour-problem/)
- [ ] [Check Knight Tour Configuration - LeetCode 2596](https://leetcode.com/problems/check-knight-tour-configuration/)

### 🧩 Practice
- [ ] [Minimum Knight Moves - LeetCode 1197](https://leetcode.com/problems/minimum-knight-moves/)
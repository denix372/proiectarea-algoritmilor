# 🤖 Heuristic Algorithms & AI Search Roadmap

**Complexity & Theory Primer:**
Unlike uninformed search (like BFS or IDDFS) which explores blindly, **Informed Search** uses a heuristic function to "guess" the best direction. 
The total estimated cost is usually defined as $f(n) = g(n) + h(n)$, where:
*   $g(n)$ is the exact cost from the start node to the current node $n$.
*   $h(n)$ is the heuristic estimate of the cost from node $n$ to the goal.

To guarantee that an algorithm like A* finds the **optimal** (shortest) path, the heuristic $h(n)$ must be **admissible** (optimistic). This means it never overestimates the true cost to the goal: $h(n) \le h^*(n)$. A heuristic is even stronger if it is **consistent (monotone)**, meaning $h(n) \le h(n') + c(n, n')$, which automatically makes it admissible.

---

## SECTION 1: Irrevocable Local Search (Explorare Irevocabilă)
*Concept: These algorithms only keep track of the current state and its immediate neighbors (the OPEN list has only one element). They move strictly toward higher/better values and cannot backtrack. They are fast but not complete and not optimal, as they easily get stuck in "local optima".*

### PATTERN: Hill Climbing (Gradientul Maxim) & Simulated Annealing
*   **Hill Climbing:** Always picks the best neighbor.
*   **Simulated Annealing:** Probabilistically accepts worse moves early on to escape local maxima, slowly "cooling down" to behave like Hill Climbing.

#### Standard (AI Theory & Simulation)
*   N-Queens (Solving via Hill Climbing / Min-Conflicts) — LeetCode 51
*   Travelling Salesman Problem (Using Simulated Annealing) — GFG

#### Practice (Mathematical Optimization)
*   Find Peak Element (A basic 1D local maximum search) — LeetCode 162
*   Maximum/Minimum of a mathematical function using Hill Climbing — GFG

---

## SECTION 2: Tentative & Greedy Search (Explorare Tentativă)
*Concept: These algorithms keep a frontier of unexplored nodes (OPEN list) and often a set of explored nodes (CLOSED list). They can backtrack to previous paths if the current one looks bad (Tentative).*

### PATTERN: Greedy Best-First Search (Explorare Lacomă)
*Concept: Expands the node that appears closest to the goal, ignoring the cost taken to get there ($f(n) = h(n)$). It is fast but NOT optimal, and can get stuck in infinite loops if a CLOSED list isn't used to track visited territory.*

#### Standard
*   Minimum Path Sum (Solving via Greedy approximation before DP) — LeetCode 64
*   Cheapest Flights Within K Stops (Greedy State Exploration) — LeetCode 787

### PATTERN: Beam Search
*Concept: A memory-optimized variation of Best-First Search that only keeps the top `B` (Beam Width) best nodes in the OPEN list at any level.*

#### Practice
*   Word Ladder (Optimizing BFS with a beam width) — LeetCode 127
*   Sequence generation in Natural Language Processing (NLP) — GFG Theory

---

## SECTION 3: A* Search (Explorare Completă și Optimală)
*Concept: The crown jewel of pathfinding. Uses $f(n) = g(n) + h(n)$. If the heuristic is admissible, A* is both **complete** (will find a solution if one exists) and **optimal** (will find the best solution).*

### PATTERN: Grid Pathfinding (Euclidean & Manhattan Distance)
*Concept: Using distance heuristics to navigate 2D grids faster than standard BFS.*

#### Standard
*   Shortest Path in Binary Matrix (Perfect for A* with Chebyshev/Max distance) — LeetCode 1091
*   Path With Minimum Effort — LeetCode 1631

#### Practice
*   Minimum Obstacle Removal to Reach Corner — LeetCode 2290
*   Shortest Path in a Grid with Obstacles Elimination — LeetCode 1293

### PATTERN: State-Space Search & Dominance
*Concept: Applying A* to complex configurations (like board games). If heuristic $h_1$ is strictly greater than (more informed than) $h_2$, $A^*$ using $h_1$ will explore fewer nodes and **dominate** the search.*

#### Standard
*   Sliding Puzzle (The classic 8-Puzzle from the university course) — LeetCode 773
    *   *Note on 8-Puzzle Heuristics:* The Manhattan Distance heuristic is more informed (dominates) the Misplaced Tiles heuristic because it provides a closer estimate to the true cost without overestimating.

#### Niche
*   Minimum Number of Flips to Convert Binary Matrix to Zero Matrix — LeetCode 1284
*   Cut Off Trees for Golf Event (A* applied to multiple targets) — LeetCode 675

---

## SECTION 4: Specialized Heuristics
*Concept: Domain-specific rules of thumb designed for very specific mathematical or combinatorial problems.*

### PATTERN: Warnsdorff’s Heuristic
*Concept: A heuristic designed specifically for the Knight's Tour problem. The rule is to always move to the adjacent unvisited square with the fewest onward moves. This drastically prunes the backtracking tree.*

#### Standard
*   Knight's Tour (Warnsdorff's Algorithm) — GFG
*   Check Knight Tour Configuration — LeetCode 2596 (Validating the path)

#### Practice
*   Minimum Knight Moves (Using A* or Bidirectional BFS) — LeetCode 1197
# 🎲 Randomized Algorithms Roadmap

**Complexity Primer:**
Unlike deterministic algorithms, the runtime or correctness of randomized algorithms depends on random variables. We calculate their efficiency using **Expected Time Complexity**. Instead of finding the absolute worst-case, we calculate the average over all possible random choices using the Expected Value formula:
$$E[X] = \sum_{i} x_i P(x_i)$$
Where $x_i$ is the cost of an operation and $P(x_i)$ is the probability of that choice. For example, Randomized QuickSort avoids the worst-case O(n²) by picking a random pivot, making the *expected* depth of the recursion tree logarithmic, resulting in an expected time of O(n log n).

## SECTION: Randomized Algorithms

### PATTERN: Las Vegas Algorithms
*Concept: These algorithms ALWAYS produce the correct result, but their runtime varies based on the random choices made. You gamble with time, not correctness.*

#### 🔥 Standard (Core Mechanisms)
* Randomized QuickSort (Random Pivoting) — GFG
* Shuffle an Array (Fisher-Yates Algorithm) — LeetCode 384
* Randomized Binary Search — GFG

#### 🧩 Practice (Sampling & Generation)
* Implement Rand10() Using Rand7() — LeetCode 470
* Linked List Random Node (Reservoir Sampling) — LeetCode 382
* Make a Fair Coin from a Biased Coin (Von Neumann Extraction) — GFG

#### 🌀 Niche (Advanced Data Structures)
* Random Node from a Tree — GFG
* Random Pick with Weight — LeetCode 528
* Random Acyclic Maze Generator — GFG

---

### PATTERN: Monte Carlo Algorithms
*Concept: These algorithms have a strict, bounded runtime (they are fast), but they have a small, calculable probability of being WRONG. You gamble with correctness, not time.*

#### 🔥 Standard (Math & Estimation)
* Primality Testing (Fermat's Method) — GFG
* Miller-Rabin Primality Test — GFG (More robust than Fermat)
* Estimating the value of Pi using Monte Carlo — GFG

#### 🧩 Practice (Graphs & Matrices)
* Karger’s Algorithm for Minimum Cut — [GitHub / GFG Reference](https://github.com/topics/kargers-algorithm) (Finds a minimum cut in a graph; repeating it amplifies the probability of success).
* Freivald’s Algorithm — GFG (Checks if matrix C is the product of A and B in O(n²) time instead of O(n³)).

#### 🌀 Niche
* Randomized algorithm for Vertex Cover — GFG

---

### PATTERN: Hashing, Probabilities, & Expectations
*Concept: Using randomness to avoid collisions, detect patterns, or calculate expected events in O(N) time.*

#### 🔥 Standard (Probability Basics)
* Birthday Paradox — GFG (Understanding hash collision probabilities)
* Expected Value of an Array — GFG
* Generate 0 and 1 with 25% and 75% probability — GFG

#### 🧩 Practice (String & Text Processing)
* Polynomial Hashing (Rabin-Karp Variant) — GFG (Using a random base and prime modulus to detect a repeated line in a text in expected O(N) time).
* Index of Max Occurring Element with Equal Probability — GFG
* Generate CAPTCHA and Verify — GFG

#### 🌀 Niche (Advanced Statistics)
* Linearity of Expectation — GFG
* Expected Number of Trials until Success (Geometric Distribution) — GFG
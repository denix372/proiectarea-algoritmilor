# 🎲 Randomized Algorithms Roadmap

**Complexity Primer:**
Unlike deterministic algorithms, the runtime or correctness of randomized algorithms depends on random variables. We calculate their efficiency using **Expected Time Complexity**. Instead of finding the absolute worst-case, we calculate the average over all possible random choices using the Expected Value formula:
$$E[X] = \sum_i x_i P(x_i)$$
Where $x_i$ is the cost of an operation and $P(x_i)$ is the probability of that choice. For example, Randomized QuickSort avoids the worst-case $O(n^2)$ by picking a random pivot, making the *expected* depth of the recursion tree logarithmic, resulting in an expected time of $O(n \log n)$.

## PATTERN: Las Vegas Algorithms

[[PATTERN_CARD_HERE]]

*Concept: These algorithms ALWAYS produce the correct result, but their runtime varies based on the random choices made. You gamble with time, not correctness.*

### 🔥 Standard (Core Mechanisms)
- [x] [Randomized QuickSort (Random Pivoting) - GFG](./las_vegas/randomized_quicksort.py) — https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
- [x] [Shuffle an Array (Fisher-Yates Algorithm) - LeetCode 384](./las_vegas/shuffle_an_array.py) — https://leetcode.com/problems/shuffle-an-array/
- [x] [Randomized Binary Search - GFG](./1-las_vegas_algorithms/randomized_binary_search.py) — https://www.geeksforgeeks.org/randomized-binary-search-algorithm/

### 🧩 Practice (Sampling & Generation)
- [x] [Implement Rand10() Using Rand7() - LeetCode 470](./1-las_vegas_algorithms/implement_rand10_using_rand7.py) — https://leetcode.com/problems/implement-rand10-using-rand7/
- [x] [Linked List Random Node (Reservoir Sampling) - LeetCode 382](./las_vegas/linked_list_random_node.py) — https://leetcode.com/problems/linked-list-random-node/
- [x] [Make a Fair Coin from a Biased Coin (Von Neumann Extraction) - GFG](https://www.geeksforgeeks.org/dsa/print-0-and-1-with-50-probability/)

### 🌀 Niche (Advanced Data Structures)
- [ ] [Random Node from a Tree - GFG](https://www.geeksforgeeks.org/random-node-from-a-tree/)
- [ ] [Random Pick with Weight - LeetCode 528](https://leetcode.com/problems/random-pick-with-weight/)
- [ ] [Random Acyclic Maze Generator - GFG](https://www.geeksforgeeks.org/random-acyclic-maze-generator-with-given-entry-and-exit-point/)

---

## PATTERN: Monte Carlo Algorithms

[[PATTERN_CARD_HERE]]

*Concept: These algorithms have a strict, bounded runtime (they are fast), but they have a small, calculable probability of being WRONG. You gamble with correctness, not time.*

### 🔥 Standard (Math & Estimation)
- [x] [Primality Testing (Fermat's Method) - GFG](https://www.geeksforgeeks.org/primality-test-set-2-fermet-method/)
- [x] [Miller-Rabin Primality Test - GFG](https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/)
- [x] [Estimating the value of Pi using Monte Carlo - GFG](https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/)

### 🧩 Practice (Graphs & Matrices)
- [x] [Karger’s Algorithm for Minimum Cut - GFG](https://www.geeksforgeeks.org/introduction-and-implementation-of-kargers-algorithm-for-minimum-cut/) / [GitHub Reference](https://github.com/topics/kargers-algorithm)
- [x] [Freivald’s Algorithm - GFG](https://www.geeksforgeeks.org/dsa/freivalds-algorithm/)

### 🌀 Niche
- [ ] [Randomized algorithm for Vertex Cover - GFG](https://www.geeksforgeeks.org/randomized-algorithm-for-vertex-cover/)

---

## PATTERN: Hashing, Probabilities, & Expectations

[[PATTERN_CARD_HERE]]

*Concept: Using randomness to avoid collisions, detect patterns, or calculate expected events in $O(N)$ time.*

### 🔥 Standard (Probability Basics)
- [x] [Birthday Paradox - GFG](./3-hashing_probabilities_expectations/birthday_paradox.py) — https://www.geeksforgeeks.org/birthday-paradox/
- [x] [Expected Value of an Array - GFG](https://www.geeksforgeeks.org/dsa/expectation-expected-value-array/)
- [x] [Generate 0 and 1 with 25% and 75% probability - GFG](./3-hashing_probabilities_expectations/generate_0_and_1_with_25_and_75_probability.py) — https://www.geeksforgeeks.org/generate-0-1-25-75-probability/

### 🧩 Practice (String & Text Processing)
- [x] [Polynomial Hashing (Rabin-Karp Variant) - GFG](https://www.geeksforgeeks.org/string-hashing-using-polynomial-rolling-hash-function/)
- [x] [Index of Max Occurring Element with Equal Probability - GFG](https://www.geeksforgeeks.org/dsa/find-index-maximum-occurring-element-equal-probability/)
- [x] [Generate CAPTCHA and Verify - GFG](https://www.geeksforgeeks.org/dsa/program-generate-captcha-verify-user/)

### 🌀 Niche (Advanced Statistics)
- [ ] [Linearity of Expectation - GFG](https://www.geeksforgeeks.org/linearity-of-expectation/)
- [ ] [Expected Number of Trials until Success (Geometric Distribution) - GFG](https://www.geeksforgeeks.org/expected-number-of-trials-before-success/)
# Backtracking — Complete Roadmap

This is the complete list of backtracking problems, organized by phases.  
Use the GitHub Issue for tracking progress.

---

# Phase 1 — The Core Three (Subsets, Permutations, Combinations)

These are the building blocks of almost all backtracking.  
Master these before moving on.

## Standard (Core Mechanics)
- Subsets — LeetCode 78 / GFG https://leetcode.com/problems/subsets/
- Permutations — LeetCode 46/ GFG https://leetcode.com/problems/permutations/description/
- Combinations — LeetCode 77 / GFG https://leetcode.com/problems/combinations/
- Combination Sum — LeetCode 38 https://leetcode.com/problems/combination-sum/description/
- Arrangements/ K-Permutations — Permutations with length K
- Cartesian Product between lists

## Practice
- Subsets — LeetCode 90 https://leetcode.com/problems/subsets-ii/
- Permutations II (With duplicates) — LeetCode 47 https://leetcode.com/problems/permutations-ii/
- Combination Sum II (With duplicates, use each once) — LeetCode 40 https://leetcode.com/problems/combination-sum-ii/
- Combination Sum III — Leetcode 216 https://leetcode.com/problems/combination-sum-iii/description/
- Letter Combinations of a Phone Number - Leetcode 17 https://leetcode.com/problems/letter-combinations-of-a-phone-number/
- Generate Parantheses — Leetcode 22 https://leetcode.com/problems/generate-parentheses/description/
- Power Set in Lexicographic Order — GFG https://www.geeksforgeeks.org/dsa/powet-set-lexicographic-order/


## Niche (Save these for last)
- K-th Permutation Sequence — LeetCode 60 - https://leetcode.com/problems/permutation-sequence/description/
- Combination Sum IV (DP problem but good recursion practice) — LeetCode 377
- String generation with frequency and K consecutive constraints — Romanian
- Permutations of a String (Lexicographic order) — [GFG](https://www.geeksforgeeks.org/problems/permutations-of-a-given-string-1587115620/1)

---

# Phase 2 — Constraint Satisfaction & Board Games

## Standard (Core Mechanics)
- N-Queens — Leetcode 51 https://leetcode.com/problems/n-queens/description/
- Word Search — Leetcode 79 https://leetcode.com/problems/word-search/
- Rat in a Maze — https://www.geeksforgeeks.org/dsa/rat-in-a-maze/
- Sudoku Solver — https://leetcode.com/problems/sudoku-solver/


## Practice
- N-Queens II - LeetCode 52 https://leetcode.com/problems/n-queens-ii/
- M-Coloring Problem https://www.geeksforgeeks.org/dsa/m-coloring-problem/
- N-Queen in O(n) space — GFG https://www.geeksforgeeks.org/dsa/n-queen-in-on-space/
- Knight’s Tour (Warnsdorff heuristic) — GFG https://www.geeksforgeeks.org/dsa/warnsdorffs-algorithm-knights-tour-problem/
- Knight’s Tour — CSES 1689 https://cses.fi/problemset/submit/1689/
- Unique Paths III — LeetCode 980 https://leetcode.com/problems/unique-paths-iii/description/

## Niche
- Solving Cryptarithmetic Puzzles (SEND + MORE = MONEY) — [GFG](https://www.geeksforgeeks.org/dsa/solving-cryptarithmetic-puzzles/)
- Hamiltonian Cycle — GFG
- Magnet Puzzle — GFG
- Sudoku (Print all solutions) — GFG
- Gray Code — CSES 2205 https://cses.fi/problemset/task/2205
- Tiling Rectangle — https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

---

# Phase 3 — Partitioning & Optimization

These problems involve splitting strings or sets into valid pieces.

## Standard (Do these as fast as possible)
- Palindrome Partitioning — LeetCode 131 https://leetcode.com/problems/palindrome-partitioning/
- Word Break I (Backtracking version first) — LeetCode 139 https://leetcode.com/problems/word-break/
- Word Break II — LeetCode 140 https://leetcode.com/problems/word-break-ii/description/

## Practice
- Partition to K Equal Sum Subsets — LeetCode 698 (Backtracking version first) https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
- Subset Sum (Backtracking version first)  — GFG  https://www.geeksforgeeks.org/dsa/subset-sum-problem-dp-25/
- Remove Invalid Parentheses — LeetCode 301 / GFG https://leetcode.com/problems/remove-invalid-parentheses/description/
- All Palindromic Partitions (with memoization) —  https://www.geeksforgeeks.org/dsa/given-a-string-print-all-possible-palindromic-partition/

## Niche
- Word Squares — [LeetCode 425](https://leetcode.ca/all/425.html) 
- Tug of War — [GFG](https://www.geeksforgeeks.org/dsa/tug-of-war/)
- All Longest Common Subsequences in Lexicographical Order — [GFG](https://www.geeksforgeeks.org/dsa/print-longest-common-sub-sequences-lexicographical-order/)

---

# Phase 4 — Pathfinding & Complex Exploration

Harder problems involving distance, safety, or complex state tracking.

## Standard (Do these as fast as possible)
- Rat in a Maze with multiple jumps — GFG https://www.geeksforgeeks.org/dsa/rat-in-a-maze-with-multiple-steps-jump-allowed/
- Combinational Sum/Target Sum Combinations (Variation of standard combination sum) — GFG
https://www.geeksforgeeks.org/dsa/combinational-sum/

## Practice
- Longest Possible Route in a Matrix with Hurdles — GFG https://www.geeksforgeeks.org/dsa/longest-possible-route-in-a-matrix-with-hurdles/
- Shortest Safe Route with Landmines (Backtracking version first) —  GFG https://www.geeksforgeeks.org/dsa/find-shortest-safe-route-in-a-path-with-landmines/
- Maximum Number Possible with at-most K Swaps — GFG https://www.geeksforgeeks.org/dsa/find-maximum-number-possible-by-doing-at-most-k-swaps/

## Niche
- Paths from corner cell to middle cell — [GFG](https://www.geeksforgeeks.org/dsa/find-paths-from-corner-cell-to-middle-cell-in-maze/)
- All paths between two vertices (Graph Backtracking) — [GFG](https://www.geeksforgeeks.org/dsa/count-possible-paths-two-vertices/#expected-approach-using-dfs-and-memoization-ov-e-time-and-ov-space)
- Path of more than k length from a source — [GFG](https://www.geeksforgeeks.org/dsa/find-if-there-is-a-path-of-more-than-k-length-from-a-source/)
- All paths from a given source to a destination — GFG

---

# Phase 5 — Advanced Constraint Pruning (Niche Layer)

specific or advanced competitive programming techniques.

- [N-Queens with AC3 (Arc Consistency Algorithm) — GFG](https://www.geeksforgeeks.org/artificial-intelligence/constraint-propagation-in-ai/) 
- Check for Sum-String — GFG

---

# TOTAL: Backtracking Roadmap (55 problems)

---
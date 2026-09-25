# 📖 Theory Roadmap: Backtracking

> 🔗 **[← Back to Problem List](./readme.md)**
>
> **Backtracking** = Exhaustive search with **pruning**. Build a solution incrementally; abandon ("backtrack") a branch as soon as it violates a constraint. It explores the **implicit decision tree** of all possibilities.

---

## 🔑 The Universal Backtracking Template

```
function backtrack(state, choices):
    if state is a complete solution:
        record(state)
        return

    for choice in choices:
        if choice is valid:
            make(choice)            # modify state
            backtrack(state, remaining_choices)
            undo(choice)            # restore state  ← THE KEY STEP
```

> ⚡ **Pruning** = adding conditions inside the `for` loop that skip branches early, reducing the exponential search space dramatically.

---

## PATTERN 1 — The Core Three: Subsets, Permutations, Combinations

---

### 🧠 Recognize It When…
- "Find all subsets / power set."
- "All permutations of a list."
- "All combinations of size K summing to target."

---

### 💡 Subsets (Power Set)

State: current subset. At each step, decide to **include or exclude** the next element.

```
result = []
function subsets(start, current):
    result.append(list(current))       # every prefix is a valid subset
    for i in range(start, len(nums)):
        current.append(nums[i])
        subsets(i + 1, current)        # i+1 ensures no reuse
        current.pop()                  # undo
```

| | Time | Space |
|--|--|--|
| Subsets | O(2^n × n) | O(n) recursion depth |

---

### 💡 Permutations

State: current permutation. At each step, choose any **unused** element.

```
result = []; used = [False] * n
function permutations(current):
    if len(current) == n:
        result.append(list(current)); return
    for i in range(n):
        if used[i]: continue
        # Skip duplicates: if nums[i] == nums[i-1] and not used[i-1]
        used[i] = True
        current.append(nums[i])
        permutations(current)
        current.pop()
        used[i] = False
```

| | Time | Space |
|--|--|--|
| Permutations | O(n! × n) | O(n) |

---

### 💡 Combinations / Combination Sum

State: current combination. Advance the start index to avoid reuse (or keep the same index for unbounded).

```
result = []
function combine(start, current, remaining):
    if remaining == 0:
        result.append(list(current)); return
    for i in range(start, len(candidates)):
        if candidates[i] > remaining: break    # pruning (if sorted)
        current.append(candidates[i])
        combine(i + 1, current, remaining - candidates[i])  # i for unbounded
        current.pop()
```

| | Time | Space |
|--|--|--|
| Combinations | O(C(n,k) × k) | O(k) |
| Combination Sum | O(n^(target/min)) | O(target/min) |

---

## PATTERN 2 — Constraint Satisfaction & Board Games

---

### 🧠 Recognize It When…
- Place items on a board with global constraints (no two queens attack each other).
- "N-Queens", "Sudoku", "Word Search on a grid."

---

### 💡 N-Queens

Place one queen per row. Track which **columns** and **diagonals** are occupied. Prune immediately if placing a queen conflicts.

```
cols = set(); diag1 = set(); diag2 = set()
result = []

function placeQueens(row, board):
    if row == n:
        result.append(board_to_string(board)); return
    for col in range(n):
        if col in cols or (row-col) in diag1 or (row+col) in diag2:
            continue    # pruning: invalid placement
        cols.add(col); diag1.add(row-col); diag2.add(row+col)
        board[row][col] = 'Q'
        placeQueens(row + 1, board)
        board[row][col] = '.'
        cols.remove(col); diag1.remove(row-col); diag2.remove(row+col)
```

---

### 💡 Word Search (Grid DFS)

From each cell, DFS in 4 directions. Mark visited cells to avoid reuse; unmark on backtrack.

```
function search(r, c, k):     # k = index in word
    if k == len(word): return True
    if out_of_bounds(r, c) or visited[r][c] or board[r][c] ≠ word[k]:
        return False
    visited[r][c] = True
    found = any(search(r+dr, c+dc, k+1) for dr,dc in directions)
    visited[r][c] = False     # undo
    return found
```

---

### 💡 Sudoku Solver

For each empty cell, try digits 1-9. Place a digit if it's valid in the row, column, and 3×3 box. Backtrack if no digit works.

```
function solve(board):
    for each empty cell (r, c):
        for d in '123456789':
            if isValid(board, r, c, d):
                board[r][c] = d
                if solve(board): return True
                board[r][c] = '.'    # undo
        return False    # no digit worked → backtrack
    return True    # no empty cell → solved
```

| | Worst Time | Space |
|--|--|--|
| N-Queens | O(n!) | O(n) |
| Word Search | O(m×n × 4^L) — L=word length | O(L) |
| Sudoku | O(9^(empty cells)) | O(1) |

---

## PATTERN 3 — Partitioning & Optimization

---

### 🧠 Recognize It When…
- "Partition a string into parts, each satisfying a property."
- "Find all ways to break a string into dictionary words."

---

### 💡 Palindrome Partitioning

At each position, try all lengths for the next partition segment. Only proceed if the current segment is a palindrome.

```
result = []
function partition(start, current):
    if start == len(s):
        result.append(list(current)); return
    for end in range(start + 1, len(s) + 1):
        if isPalindrome(s, start, end - 1):
            current.append(s[start:end])
            partition(end, current)
            current.pop()
```

---

### 💡 Word Break (Backtracking → then Memoize)

Try each word in the dictionary as the next segment. Memoize failed positions to avoid exponential blowup.

```
memo = {}
function wordBreak(start):
    if start == len(s): return [[]]
    if start in memo: return memo[start]
    results = []
    for word in wordDict:
        if s[start:].startswith(word):
            for sentence in wordBreak(start + len(word)):
                results.append([word] + sentence)
    memo[start] = results
    return results
```

| | Complexity |
|--|--|
| Palindrome Partitioning | O(n × 2^n) worst, O(n²) with DP precompute |
| Word Break II | O(n² × |dict|) with memoization |

---

## PATTERN 4 — Pathfinding & Complex Exploration

---

### 🧠 Recognize It When…
- Find **all paths** or the **longest path** in a grid/graph (no polynomial algorithm exists without backtracking).
- State requires tracking the exact path taken.

---

### 💡 All Paths / Longest Path in Grid

DFS with full path tracking. Backtrack by unmarking visited cells.

```
function dfs(r, c, steps):
    if (r, c) is destination:
        max_steps = max(max_steps, steps); return
    visited[r][c] = True
    for each neighbor (nr, nc):
        if not visited[nr][nc] and is_valid(nr, nc):
            dfs(nr, nc, steps + 1)
    visited[r][c] = False    # backtrack
```

> 💡 Unlike shortest-path problems (BFS), longest-path problems on general graphs are NP-Hard, so backtracking is the correct approach for small inputs.

---

## PATTERN 5 — Advanced Constraint Pruning

---

### 🧠 Recognize It When…
- Complex constraint propagation before recursion (like AC-3 for CSPs).
- Domain-specific pruning far beyond simple bound checks.

---

### 💡 Forward Checking

Before making a choice, propagate constraints to eliminate invalid options in future steps. If any variable's domain becomes empty, prune immediately.

```
function backtrackWithForwardChecking(assignment, domains):
    if assignment is complete: return assignment
    var = selectUnassignedVariable(assignment, domains)
    for value in domains[var]:
        if consistent(assignment, var, value):
            assignment[var] = value
            new_domains = propagate_constraints(domains, var, value)
            if no domain is empty:
                result = backtrackWithForwardChecking(assignment, new_domains)
                if result ≠ failure: return result
            del assignment[var]
    return failure
```

> 🔑 **Arc Consistency (AC-3)**: Ensures that for every value in a variable's domain, there exists at least one compatible value in every neighboring variable's domain. Used in advanced N-Queens and Sudoku solvers.

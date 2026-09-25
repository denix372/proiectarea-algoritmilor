# 📖 Theory Roadmap: Game Algorithms

> 🔗 **[← Back to Problem List](./readme.md)**
>
> Game algorithms deal with **two-player zero-sum games** where one player's gain equals the other's loss. The goal is to find the **optimal strategy** — the move that maximizes your score assuming the opponent plays perfectly.

---

## 🔑 Core Concepts at a Glance

| Concept | When to Use |
|---------|-------------|
| **Nim / Sprague-Grundy** | Combinatorial games with token removal |
| **Minimax** | State-space tree search for optimal play |
| **Negamax** | Unified Minimax (eliminates code duplication) |
| **Alpha-Beta Pruning** | Cut off branches worse than known solutions |
| **Iterative Deepening** | Explore progressively deeper with time limit |
| **Zobrist Hashing** | Cache game states efficiently |

---

## PATTERN 1 — The Game of Nim & Grundy Numbers

---

### 🧠 Recognize It When…
- Two players take turns removing tokens from piles.
- The player who takes the last token wins (or loses — "misère" variant).
- Need to determine if the **current player** wins with optimal play.

---

### 💡 Nim Game

**Key Theorem**: The current player **LOSES** if and only if the XOR of all pile sizes equals **0** (called a "P-position" or "Nim-sum = 0").

```
def nimWinner(piles):
    xor_sum = 0
    for pile in piles:
        xor_sum ^= pile
    return xor_sum != 0   # True = current player wins
```

> **Why XOR?** After XOR-ing all piles, if `nim_sum ≠ 0`, the current player can always make a move that makes `nim_sum = 0`. From `nim_sum = 0`, any move creates `nim_sum ≠ 0`, giving the advantage back.

---

### 💡 Sprague-Grundy Theorem

Every **impartial game** (both players have same moves) can be assigned a **Grundy number (nimber)** `G(state)`:

- `G(state) = 0` → the current player **loses** (P-position)
- `G(state) > 0` → the current player **wins** (N-position)

`G(state) = MEX({G(next_state) for all moves})` where MEX = Minimum EXcludant (smallest non-negative integer not in the set).

```
def grundy(state, memo={}):
    if state in memo: return memo[state]
    reachable = {grundy(next_state) for next_state in get_moves(state)}
    g = 0
    while g in reachable: g += 1   # MEX
    memo[state] = g
    return g
```

**Compound games**: XOR the Grundy numbers of each sub-game. If XOR ≠ 0, current player wins.

| | Complexity |
|--|--|
| Nim winner check | O(n) — n piles |
| Grundy computation | O(states × moves) |

---

## PATTERN 2 — Core Minimax & Negamax

---

### 🧠 Recognize It When…
- Two-player, perfect information, zero-sum game.
- "Can the first player win?", "what is the optimal score?"
- Tic-Tac-Toe, Chess, Connect Four.

---

### 💡 Minimax

The **maximizing** player picks the move with the highest value; the **minimizing** player picks the lowest.

```
function minimax(state, depth, isMaximizing):
    if isTerminal(state) or depth == 0:
        return evaluate(state)

    if isMaximizing:
        best = -infinity
        for move in getMoves(state):
            best = max(best, minimax(apply(state, move), depth-1, False))
        return best
    else:
        best = +infinity
        for move in getMoves(state):
            best = min(best, minimax(apply(state, move), depth-1, True))
        return best
```

---

### 💡 Negamax (Simplified Minimax)

Since the score is symmetric (what's good for MAX is bad for MIN), use: `score = -negamax(child)`.

```
function negamax(state, depth):
    if isTerminal(state) or depth == 0:
        return evaluate(state) * sign(currentPlayer)

    best = -infinity
    for move in getMoves(state):
        score = -negamax(apply(state, move), depth - 1)
        best = max(best, score)
    return best
```

| | Complexity |
|--|--|
| Time | O(b^d) — b = branching factor, d = depth |
| Space | O(d) |

---

## PATTERN 3 — Optimization: Pruning & Hashing

---

### 🧠 Recognize It When…
- Minimax tree is too large to fully explore.
- Need to speed up game tree search.

---

### 💡 Alpha-Beta Pruning

Maintain a window `[alpha, beta]`:
- `alpha` = best score the **maximizer** is guaranteed (lower bound).
- `beta` = best score the **minimizer** is guaranteed (upper bound).
- **Prune** when `alpha >= beta` — the current branch cannot improve the result.

```
function alphaBeta(state, depth, alpha, beta, isMaximizing):
    if isTerminal(state) or depth == 0:
        return evaluate(state)

    if isMaximizing:
        for move in getMoves(state):
            alpha = max(alpha, alphaBeta(child, depth-1, alpha, beta, False))
            if alpha >= beta: break   # ✂️ PRUNE (beta cutoff)
        return alpha
    else:
        for move in getMoves(state):
            beta = min(beta, alphaBeta(child, depth-1, alpha, beta, True))
            if alpha >= beta: break   # ✂️ PRUNE (alpha cutoff)
        return beta

# Initial call:
alphaBeta(root, depth, -infinity, +infinity, True)
```

> 🚀 **Best case**: Reduces from O(b^d) to **O(b^(d/2))** — effectively doubles the searchable depth with the same time budget. Requires **move ordering** (try best moves first) to achieve this.

---

### 💡 Iterative Deepening (IDDFS)

Search to depth 1, 2, 3, ... until time runs out. Uses a **heuristic evaluation function** for non-terminal nodes.

```
for depth in range(1, MAX_DEPTH):
    score = alphaBeta(root, depth, -inf, +inf, True)
    if time_expired: break
best_move = last completed depth's best move
```

> ✅ Advantages: Always finds the best move within time, natural anytime algorithm.  
> ⚠️ Nodes at depth d-1 are recomputed when searching depth d — but since the tree grows exponentially, the cost of the last level dominates (overhead ≈ b/(b-1) ≈ tiny).

---

### 💡 Zobrist Hashing (Transposition Table)

Assign a random 64-bit number to each (piece, square) pair. XOR all occupied positions to get a board hash. Use a hash table to cache evaluated positions and avoid recomputation.

```
# Init: zobrist_table[piece][square] = random 64-bit int
hash = 0
for piece, square in board:
    hash ^= zobrist_table[piece][square]

# After a move (piece from sq1 to sq2):
hash ^= zobrist_table[piece][sq1]   # remove from old square
hash ^= zobrist_table[piece][sq2]   # add to new square

# Lookup before computing:
if hash in transposition_table:
    return transposition_table[hash]
```

> **Key property**: XOR is its own inverse — updating the hash after a move is O(1).

---

## PATTERN 4 — Stone Games & Array Reductions

---

### 🧠 Recognize It When…
- Players alternately pick from the **ends** of an array.
- "Stone Game", "predict the winner."

---

### 💡 Stone Game / Predict the Winner (DP)

`dp[i][j]` = maximum **score difference** (current player - other player) achievable from subarray `arr[i..j]`.

```
dp[i][i] = arr[i]   # only one element, take it
for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = max(arr[i] - dp[i+1][j],   # take left
                       arr[j] - dp[i][j-1])    # take right

# First player wins if dp[0][n-1] >= 0
```

> 🔑 **Stone Game insight**: With even number of piles and optimal play, the first player can always **guarantee at least as much** as the second (the first player can always pick all "odd-indexed" or all "even-indexed" piles, whichever is larger).

| | Complexity |
|--|--|
| Time | O(n²) |
| Space | O(n²) or O(n) rolling |

---

## PATTERN 5 — Cyclic Simulation & Probability

---

### 🧠 Recognize It When…
- Circular elimination games (Josephus), probability-based winners.
- "Who wins the game of circular removal?"

---

### 💡 Josephus Problem

`n` people in a circle; every `k`-th person is eliminated. Find the position of the last survivor.

```
# Recursive: J(1, k) = 0
#            J(n, k) = (J(n-1, k) + k) % n
def josephus(n, k):
    if n == 1: return 0
    return (josephus(n - 1, k) + k) % n
# Add 1 for 1-indexed result
```

> For **k=2** (special case): `J(n, 2) = 2L + 1` where `n = 2^m + L`.

| | Complexity |
|--|--|
| Time | O(n) recursive / O(log n) for k=2 |
| Space | O(n) recursive / O(1) iterative |

---

### 💡 Win Probability (Iterative Shooting Games)

Player A hits with probability `p`, Player B with probability `q`. A shoots first. What is P(A wins)?

```
# A fires at B, B fires at A, alternating
# P(A wins) = p / (p + q - p*q)   [closed form for simple case]

# General simulation:
P_A_wins = p + (1-p)*(1-q)*P_A_wins
# Solve: P_A_wins = p / (p + q - p*q)
```

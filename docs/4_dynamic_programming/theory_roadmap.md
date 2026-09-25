# 📖 Theory Roadmap: Dynamic Programming

> 🔗 **[← Back to Problem List](./readme.md)**
>
> **Dynamic Programming** = Recursion + Memoization. Break a problem into overlapping subproblems, solve each once, and store the result. It works when the problem has **Optimal Substructure** and **Overlapping Subproblems**.

---

## 🔑 DP Design Framework

1. **Define the state**: What does `dp[i]` or `dp[i][j]` represent?
2. **Write the recurrence**: How does `dp[i]` depend on smaller states?
3. **Base cases**: What are the trivial answers?
4. **Fill order**: Ensure smaller states are computed before larger ones.
5. **Answer**: Where in the DP table is the final answer?

> 🔄 **Top-Down** (Memoization): Recurse normally, cache results.  
> ⬆️ **Bottom-Up** (Tabulation): Fill the DP table iteratively.

---

## PATTERN 1 — Warmup & 1D Linear DP

---

### 🧠 Recognize It When…
- Current state depends on 1-2 previous states.
- "Fibonacci-like", "Climbing Stairs", "House Robber."

---

### 💡 Linear DP Template

```
dp[0] = base_case_0
dp[1] = base_case_1
for i in range(2, n+1):
    dp[i] = f(dp[i-1], dp[i-2], ...)   # recurrence
```

**Climbing Stairs** (`dp[i] = dp[i-1] + dp[i-2]`):  
**House Robber** (`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`):

```
# House Robber — space optimized
prev2, prev1 = 0, 0
for num in nums:
    curr = max(prev1, prev2 + num)
    prev2, prev1 = prev1, curr
return prev1
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) with rolling variables |

---

## PATTERN 2 — DP on Grids

---

### 🧠 Recognize It When…
- 2D grid, can only move right/down (or limited directions).
- "Number of paths", "minimum path sum", "maximal square."

---

### 💡 Grid DP Template

```
dp[0][0] = grid[0][0]
# Fill first row and column (base cases)
for i in range(1, m): dp[i][0] = dp[i-1][0] + grid[i][0]
for j in range(1, n): dp[0][j] = dp[0][j-1] + grid[0][j]

# Fill rest
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
```

**Maximal Square** (`dp[i][j]` = side of largest square with bottom-right at `(i,j)`):
```
if grid[i][j] == '1':
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
```

| | Complexity |
|--|--|
| Time | O(m × n) |
| Space | O(m × n) or O(n) with rolling row |

---

## PATTERN 3 — DP on Strings

---

### 🧠 Recognize It When…
- Two strings, looking for common subsequence, edit distance, or matching.
- `dp[i][j]` represents something about the first `i` characters of `s1` and first `j` of `s2`.

---

### 💡 Longest Common Subsequence (LCS)

```
dp[i][j] = length of LCS of s1[0..i-1] and s2[0..j-1]

if s1[i-1] == s2[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

---

### 💡 Edit Distance (Levenshtein)

```
dp[i][j] = min edits to convert s1[0..i-1] to s2[0..j-1]

if s1[i-1] == s2[j-1]:
    dp[i][j] = dp[i-1][j-1]           # no edit needed
else:
    dp[i][j] = 1 + min(
        dp[i-1][j],    # delete from s1
        dp[i][j-1],    # insert into s1
        dp[i-1][j-1]   # replace
    )
```

---

### 💡 Longest Palindromic Substring (Expand or DP)

```
# DP approach: dp[i][j] = True if s[i..j] is palindrome
for i in range(n-1, -1, -1):
    for j in range(i, n):
        if s[i] == s[j]:
            dp[i][j] = (j - i <= 2) or dp[i+1][j-1]
```

| | Time | Space |
|--|--|--|
| LCS | O(m × n) | O(m × n) |
| Edit Distance | O(m × n) | O(min(m,n)) |
| Palindrome | O(n²) | O(n²) |

---

## PATTERN 4 — Distinct Ways / Combinatorics

---

### 🧠 Recognize It When…
- "How many ways to ...", "count the number of paths/arrangements."
- Dice rolls, coin combinations, knight moves.

---

### 💡 Core Template (Combination Sum IV / Dice)

```
dp[0] = 1   # 1 way to make sum=0: use nothing
for target in range(1, total+1):
    for choice in choices:
        if choice <= target:
            dp[target] += dp[target - choice]
```

**Binomial Coefficient** `C(n, k) = C(n-1, k-1) + C(n-1, k)`:
```
dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
```

| | Complexity |
|--|--|
| Combination Sum IV | O(target × |choices|) |
| Binomial Coefficient | O(n × k) |

---

## PATTERN 5 — Knapsack Patterns

---

### 🧠 Recognize It When…
- Select items with weights/profits, limited capacity.
- "Partition into two equal subsets", "coin change."

---

### 💡 0/1 Knapsack (Each item used at most once)

```
dp[j] = max value with capacity j
for item in items:
    for j in range(W, item.weight - 1, -1):   # reverse to avoid reuse!
        dp[j] = max(dp[j], dp[j - item.weight] + item.value)
```

---

### 💡 Unbounded Knapsack (Each item used any number of times)

```
for j in range(item.weight, W + 1):   # forward — allows reuse
    dp[j] = max(dp[j], dp[j - item.weight] + item.value)
```

---

### 💡 Coin Change (Min coins)

```
dp = [infinity] * (amount + 1); dp[0] = 0
for coin in coins:
    for j in range(coin, amount + 1):
        dp[j] = min(dp[j], dp[j - coin] + 1)
return dp[amount] if dp[amount] != infinity else -1
```

---

### 💡 Partition Equal Subset Sum

Reduce to: "Can we select elements that sum to `total/2`?" — Boolean 0/1 knapsack.

```
target = sum(nums) // 2
dp = {0}   # set of reachable sums
for num in nums:
    dp = dp | {s + num for s in dp}
return target in dp
```

| Variant | Time | Space |
|---------|------|-------|
| 0/1 Knapsack | O(n × W) | O(W) |
| Unbounded | O(n × W) | O(W) |
| Coin Change | O(amount × |coins|) | O(amount) |

---

## PATTERN 6 — LIS Variants (Longest Increasing Subsequence)

---

### 🧠 Recognize It When…
- Find/count the longest subsequence with a monotone property.
- "Russian Doll Envelopes", "Jump Game", "Longest Divisible Subset."

---

### 💡 LIS — O(n²) DP

```
dp[i] = length of LIS ending at index i
dp[i] = 1 + max(dp[j] for j < i if arr[j] < arr[i])
answer = max(dp)
```

---

### 💡 LIS — O(n log n) with Patience Sorting

Maintain a `tails` array: `tails[i]` = smallest tail of all increasing subsequences of length `i+1`. Binary search for the insertion position of each element.

```
tails = []
for x in arr:
    pos = bisect_left(tails, x)   # find leftmost position >= x
    if pos == len(tails): tails.append(x)
    else: tails[pos] = x
return len(tails)
```

| | Time | Space |
|--|--|--|
| O(n²) DP | O(n²) | O(n) |
| O(n log n) | O(n log n) | O(n) |

---

## PATTERN 7 — Multi-State / State Machine DP

---

### 🧠 Recognize It When…
- Multiple possible states at each step (e.g., holding/not holding a stock).
- "Best time to buy/sell stock", "wiggle subsequence."

---

### 💡 State Machine Template

Define states explicitly. At each step, transition between states.

```
# Stock Buy/Sell with Cooldown
hold = -infinity    # best profit while holding a stock
free = 0            # best profit while in cooldown
rest = 0            # best profit while resting
for price in prices:
    new_hold = max(hold, rest - price)   # buy or keep holding
    new_free = hold + price              # sell
    new_rest = max(rest, free)           # cooldown or rest
    hold, free, rest = new_hold, new_free, new_rest
return max(free, rest)
```

---

### 💡 Maximum Product Subarray

Track both `max_prod` and `min_prod` (since a negative × negative = positive).

```
max_prod = min_prod = result = nums[0]
for x in nums[1:]:
    candidates = (x, max_prod * x, min_prod * x)
    max_prod = max(candidates)
    min_prod = min(candidates)
    result = max(result, max_prod)
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) |

---

## PATTERN 8 — Interval DP

---

### 🧠 Recognize It When…
- Optimize over a range `[i, j]` that you split into two parts.
- "Matrix Chain Multiplication", "Burst Balloons", "Palindrome Partitioning."

---

### 💡 Interval DP Template

```
# Solve for all lengths, from short to long
dp[i][i] = base_case   # single element

for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = best over all splits k in [i, j-1]:
            dp[i][j] = min/max(dp[i][k] + dp[k+1][j] + cost(i,k,j))
```

**Burst Balloons** (reverse thinking — pick the **last** balloon to burst in range `[l, r]`):
```
for length in range(1, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i, j+1):
            dp[i][j] = max(dp[i][j],
                dp[i][k-1] + val[i-1]*val[k]*val[j+1] + dp[k+1][j])
```

| | Complexity |
|--|--|
| Time | O(n³) |
| Space | O(n²) |

---

## PATTERN 9 — Advanced DP

---

### 🧠 Recognize It When…
- Numbers with digit constraints ("count numbers ≤ N with property X").
- Bitmask DP when sets of items matter (TSP, Hamiltonian paths).

---

### 💡 Digit DP

Count numbers in `[1, N]` satisfying a property by processing digits one by one.

```
State: (position, tight, ...other_state...)
# "tight" = True if we're still bounded by the digits of N

function count(pos, tight, state):
    if pos == len(digits): return is_valid(state)
    limit = digits[pos] if tight else 9
    result = 0
    for d in range(0, limit + 1):
        result += count(pos+1, tight and d==limit, update(state, d))
    return result
```

---

### 💡 Bitmask DP (TSP / Subset Problems)

State = `(current_node, visited_mask)`. Each bit in the mask represents whether a city has been visited.

```
# TSP: minimum cost Hamiltonian path
dp[mask][i] = min cost to visit all cities in mask, ending at city i

for mask in range(1, 1 << n):
    for i in range(n):
        if not (mask >> i & 1): continue
        for j in range(n):
            if mask >> j & 1: continue
            new_mask = mask | (1 << j)
            dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + dist[i][j])
```

| | Complexity |
|--|--|
| Digit DP | O(D × states) — D = number of digits |
| Bitmask DP | O(2^n × n²) |

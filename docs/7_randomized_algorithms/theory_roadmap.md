# 📖 Theory Roadmap: Randomized Algorithms

> 🔗 **[← Back to Problem List](./readme.md)**
>
> **Randomized Algorithms** use random choices during execution. Unlike deterministic algorithms, their performance is analyzed using **probability theory** and **Expected Value**.

---

## 🔑 Probability Primer

**Expected Value** of a random variable X:
$$E[X] = \sum_i x_i \cdot P(x_i)$$

**Linearity of Expectation**: `E[X + Y] = E[X] + E[Y]` — even if X and Y are *not* independent. This is the key tool for analyzing randomized algorithms.

---

## 🎲 Two Flavors of Randomized Algorithms

| Type | Correctness | Runtime | Example |
|------|-------------|---------|---------|
| **Las Vegas** | Always correct ✅ | Random (expected) | Randomized QuickSort |
| **Monte Carlo** | Probably correct ⚠️ | Always bounded | Miller-Rabin primality test |

> 🎯 Las Vegas: *"I always give you the right answer, but I might take a while."*  
> 🎯 Monte Carlo: *"I'm very fast, but I might be wrong with a small probability ε."*

---

## PATTERN 1 — Las Vegas Algorithms

---

### 🧠 Recognize It When…
- The algorithm is correct by construction, but uses randomness to **avoid worst-case inputs**.
- "Shuffle", "random pivot", "reservoir sampling."

---

### 💡 Randomized QuickSort

Instead of always picking the first/last element as pivot (vulnerable to sorted inputs), pick a **random** pivot. This makes the expected depth of the recursion tree O(log n).

```
function randomizedQuickSort(arr, lo, hi):
    if lo >= hi: return
    pivot_idx = random(lo, hi)          # random pivot!
    swap(arr[pivot_idx], arr[hi])       # move to end
    p = partition(arr, lo, hi)          # Lomuto partition
    randomizedQuickSort(arr, lo, p - 1)
    randomizedQuickSort(arr, p + 1, hi)
```

> **Expected Time**: O(n log n) — The random pivot makes the expected split balanced.  
> **Worst Case**: O(n²) — but with vanishingly small probability.

| | Expected | Worst |
|--|--|--|
| Time | O(n log n) | O(n²) |
| Space | O(log n) | O(n) |

---

### 💡 Fisher-Yates Shuffle (Uniform Random Permutation)

Generate a uniformly random permutation in O(n). At each step, swap the current element with a random one from the **remaining** elements.

```
for i from n-1 down to 1:
    j = random(0, i)        # random index in [0..i]
    swap(arr[i], arr[j])
```

> 🔑 **Why it works**: After step `k`, the last `k` positions hold a uniformly random sample — each of the `n!` permutations is equally likely.

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) |

---

### 💡 Reservoir Sampling (Random Element from Unknown-Size Stream)

Select `k` random items from a stream of unknown length `n`, with each element having equal probability `k/n`.

```
reservoir = first k elements
for i in range(k, n):
    j = random(0, i)        # random index in [0..i]
    if j < k:
        reservoir[j] = stream[i]   # replace
```

> **Invariant**: After processing element `i`, each element seen so far has probability `k/(i+1)` of being in the reservoir.

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(k) |

---

### 💡 Rand10 from Rand7 (Rejection Sampling)

Generate a uniform random number in [1, 10] using only Rand7().  
Use two Rand7() calls to create a uniform distribution over [1, 49], then reject values > 40.

```
function rand10():
    while True:
        row = rand7()               # [1..7]
        col = rand7()               # [1..7]
        idx = (row - 1) * 7 + col  # uniform in [1..49]
        if idx <= 40:
            return ((idx - 1) % 10) + 1   # uniform in [1..10]
        # else: reject and retry
```

> **Expected calls to Rand7()**: 2 × (49/40) ≈ 2.45 per call.

---

## PATTERN 2 — Monte Carlo Algorithms

---

### 🧠 Recognize It When…
- Need a **fast** probabilistic answer that may have a small error probability.
- Primality testing, min-cut estimation, matrix verification.

---

### 💡 Miller-Rabin Primality Test

Tests if `n` is prime by checking `k` random "witnesses". If all pass, `n` is **probably prime**.  
False positive probability: ≤ `(1/4)^k`.

```
function millerRabin(n, k):
    # Write n-1 as 2^r * d
    r, d = factor_out_twos(n - 1)
    for _ in range(k):
        a = random(2, n - 2)         # random witness
        x = pow(a, d, n)             # a^d mod n
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else:
            return "Composite"       # definitely composite
    return "Probably Prime"
```

| | Complexity |
|--|--|
| Time | O(k × log²n) |
| Error Prob | ≤ (1/4)^k |

> With `k = 40`, error probability ≤ `(1/4)^40` ≈ 10^-24 — effectively zero.

---

### 💡 Monte Carlo Pi Estimation

Randomly throw darts at a unit square. Count how many land inside the inscribed circle (radius 0.5). Ratio ≈ π/4.

```
inside = 0
for _ in range(N):
    x, y = random(), random()   # uniform in [0, 1]
    if x*x + y*y <= 1:
        inside += 1
pi_estimate = 4 * inside / N
```

> **Error**: O(1/√N) — converges very slowly. Useful for illustration, not for computing π precisely.

---

### 💡 Karger's Minimum Cut Algorithm

Randomly contract edges until only 2 nodes remain. The remaining edges form a cut. Repeat many times and take the minimum.

```
function karger(graph):
    while |nodes| > 2:
        (u, v) = random edge
        merge(u, v)              # contract edge
    return count remaining edges

# Run O(n² log n) times for high confidence
min_cut = infinity
for _ in range(n² * log(n)):
    min_cut = min(min_cut, karger(graph))
```

| | Complexity (single run) | Probability of correct |
|--|--|--|
| Time | O(n²) | ≥ 2/n(n-1) |
| After O(n² log n) runs | O(n⁴ log n) | ≥ 1 - 1/n |

---

### 💡 Freivalds' Algorithm (Matrix Multiplication Verification)

Verify `A × B = C` without actually computing the product.  
Choose a random vector `r ∈ {0,1}^n`. Check if `A(Br) = Cr`.

```
function freivalds(A, B, C):
    r = random binary vector of length n
    return A @ (B @ r) == C @ r   # all O(n²)
```

> **If `AB = C`**: Always returns True.  
> **If `AB ≠ C`**: Returns False with probability ≥ 1/2.  
> Run `k` times → error probability ≤ (1/2)^k.

| | Complexity |
|--|--|
| Time | O(n²) per run vs O(n³) naive |

---

## PATTERN 3 — Hashing, Probabilities & Expectations

---

### 🧠 Recognize It When…
- Use hashing to detect duplicates or patterns in O(n) expected time.
- Calculate expected number of events (birthday paradox, collisions).

---

### 💡 Birthday Paradox

> In a group of n people, what is the probability that two share a birthday?

With `n = 23` people: probability ≈ **50%**. With `n = 70`: ≈ **99.9%**.

This is why hash collision probability is higher than intuition suggests for large tables.

```
# P(at least one collision) ≈ 1 - e^(-n²/2m)
# n = number of items, m = hash table size
# Collision very likely when n ≈ √m
```

---

### 💡 Polynomial Rolling Hash (Rabin-Karp)

Assign a hash value to a substring in O(1) using precomputed prefix hashes. Used for efficient string pattern matching.

```
# Hash of s[l..r] = sum(s[i] * BASE^(r-i)) mod MOD
hash[i] = (hash[i-1] * BASE + ord(s[i])) % MOD
pow[i]  = (pow[i-1] * BASE) % MOD

def getHash(l, r):
    return (hash[r] - hash[l-1] * pow[r-l+1]) % MOD
```

> **Expected O(n + m)** for pattern matching, with hash collisions being the "Monte Carlo" element.

| | Time | Space |
|--|--|--|
| Build | O(n) | O(n) |
| Query | O(1) | — |

---

### 💡 Geometric Distribution (Expected Trials Until Success)

If each trial succeeds with probability `p`, the **expected number of trials** until the first success is:
$$E[X] = \frac{1}{p}$$

**Example** (Rand10 from Rand7): Expected iterations = 49/40 ≈ 1.225 per call.  
**Example** (Karger's): Expected runs until min-cut = O(n²).

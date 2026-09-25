# 📖 Theory Roadmap: Common Techniques

> 🔗 **[← Back to Problem List](./readme.md)**
>
> This document is the **theory companion** covering Prefix Sum, Two Pointers, and Sliding Window — the three most universally applicable techniques in competitive programming.

---

## ➕ SECTION 1: Prefix Sum

---

### PATTERN 1 — Basic Prefix Sum & Range Queries

#### 🧠 Recognize It When…
- "Sum of elements between index `i` and `j`" needs to be answered many times.
- You see a subarray sum problem with repeated queries.

#### 💡 Core Intuition
Precompute a prefix array `P` where `P[i] = arr[0] + arr[1] + ... + arr[i-1]`.  
Any range sum `[l, r]` = `P[r+1] - P[l]` in O(1).

```
# Build prefix
P = [0] * (n + 1)
for i in range(n):
    P[i+1] = P[i] + arr[i]

# Query sum of arr[l..r]
range_sum = P[r+1] - P[l]
```

> 💡 **Key insight for "Subarray Sum = K"**: Use a HashMap storing `{prefix_sum: count}`. For each new prefix sum `s`, check if `s - K` was seen before.

```
count = 0; seen = {0: 1}; s = 0
for x in arr:
    s += x
    count += seen.get(s - K, 0)
    seen[s] = seen.get(s, 0) + 1
```

| | Complexity |
|--|--|
| Build | O(n) |
| Query | O(1) |
| Space | O(n) |

---

### PATTERN 2 — Division & Modulo with Prefix Sum

#### 🧠 Recognize It When…
- "Subarray sum divisible by K."
- "Count subarrays whose sum ≡ 0 (mod K)."

#### 💡 Core Intuition
`(P[r] - P[l]) % K == 0` ⟺ `P[r] % K == P[l] % K`.  
Track the frequency of each **remainder** seen so far. When you see a remainder again, every previous occurrence pairs with the current index to form a valid subarray.

```
seen = {0: 1}; s = 0; count = 0
for x in arr:
    s = (s + x) % K
    if s < 0: s += K    # handle negative numbers
    count += seen.get(s, 0)
    seen[s] = seen.get(s, 0) + 1
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(K) |

---

### PATTERN 3 — XOR Prefix Sum

#### 🧠 Recognize It When…
- "XOR of all elements in range `[l, r]`."
- "Count subarrays with XOR equal to a target."

#### 💡 Core Intuition
XOR has a self-inverse property: `a XOR a = 0`.  
`XOR[l..r] = prefix[r] XOR prefix[l-1]`.  
Same trick as regular prefix sum, but with XOR instead of addition.

```
P = [0] * (n + 1)
for i in range(n):
    P[i+1] = P[i] ^ arr[i]

# XOR of arr[l..r]
range_xor = P[r+1] ^ P[l]
```

> 🎭 **Bitmask prefix XOR** is used for "even/odd parity of vowels" problems: encode vowel parity as bits in an integer, treat as XOR prefix.

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(n) |

---

### PATTERN 4 — 2D Prefix Sum

#### 🧠 Recognize It When…
- Sub-matrix sum queries on a 2D grid.
- "Sum of rectangle with corners (r1,c1) and (r2,c2)."

#### 💡 Core Intuition
Use the **inclusion-exclusion** principle:  
`P[r2][c2] - P[r1-1][c2] - P[r2][c1-1] + P[r1-1][c1-1]`

```
# Build 2D prefix
for r in range(1, R+1):
    for c in range(1, C+1):
        P[r][c] = grid[r-1][c-1] + P[r-1][c] + P[r][c-1] - P[r-1][c-1]

# Query rectangle (r1,c1) to (r2,c2) (1-indexed)
result = P[r2][c2] - P[r1-1][c2] - P[r2][c1-1] + P[r1-1][c1-1]
```

| | Complexity |
|--|--|
| Build | O(R × C) |
| Query | O(1) |

---

## 👆👆 SECTION 2: Two Pointers

---

### PATTERN 1 — Opposite Direction (From Both Ends)

#### 🧠 Recognize It When…
- Sorted array + looking for a **pair** that satisfies a condition.
- "Two Sum in sorted array", palindrome check, container with most water.

#### 💡 Core Intuition
Start one pointer at each end. If the current pair satisfies the condition, great. Otherwise, move the pointer that could **improve** the condition (if sum too small → move left forward; if too big → move right backward).

```
left, right = 0, len(arr) - 1
while left < right:
    s = arr[left] + arr[right]
    if s == target:
        record answer; left++; right--
    elif s < target:
        left++
    else:
        right--
```

| | Complexity |
|--|--|
| Time | O(n) after O(n log n) sort |
| Space | O(1) |

---

### PATTERN 2 — Same Direction: Fast & Slow (In-Place Filtering)

#### 🧠 Recognize It When…
- Remove duplicates or specific elements in-place.
- "Move zeroes to end", "compact" an array.

#### 💡 Core Intuition
`slow` marks the next position to write; `fast` scans all elements. Only advance `slow` when `fast` finds a valid element to keep.

```
slow = 0
for fast in range(len(arr)):
    if arr[fast] satisfies condition:
        arr[slow] = arr[fast]
        slow++
# arr[0..slow-1] is the filtered result
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) |

---

### PATTERN 3 — Partitioning & Swapping (Quick Select Style)

#### 🧠 Recognize It When…
- Partition array around a pivot (Dutch Flag / 3-way).
- "Next permutation", "partition labels."

#### 💡 Core Intuition
**Dutch National Flag (3 colors)**: Use 3 pointers `low`, `mid`, `high`. Swap elements to their correct region.

```
# Sort Colors: 0s, 1s, 2s
low = 0; mid = 0; high = n - 1
while mid <= high:
    if arr[mid] == 0:
        swap(arr[low], arr[mid]); low++; mid++
    elif arr[mid] == 1:
        mid++
    else:
        swap(arr[mid], arr[high]); high--
```

**Next Permutation**:
1. Find the rightmost ascending pair: `arr[i] < arr[i+1]`.
2. Find the rightmost element > `arr[i]`, swap them.
3. Reverse everything after index `i`.

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) |

---

### PATTERN 4 — Merging Two Arrays / Meet in the Middle

#### 🧠 Recognize It When…
- Merge two sorted arrays in-place (or with auxiliary space).
- Pattern-matching within strings (`strStr`, sequence matching).

#### 💡 Core Intuition
**Merge Sorted Array**: Fill from the **right** to avoid overwriting. Use three pointers: `i` (end of arr1), `j` (end of arr2), `k` (end of merged).

```
i = m - 1; j = n - 1; k = m + n - 1
while i >= 0 and j >= 0:
    if arr1[i] >= arr2[j]:
        arr1[k] = arr1[i]; i--
    else:
        arr1[k] = arr2[j]; j--
    k--
while j >= 0:
    arr1[k] = arr2[j]; j--; k--
```

| | Complexity |
|--|--|
| Time | O(m + n) |
| Space | O(1) |

---

## 🪟 SECTION 3: Sliding Window

---

### PATTERN 1 — Fixed-Length Window

#### 🧠 Recognize It When…
- Window size **K** is given and fixed.
- "Maximum/minimum/average of every subarray of size K."

#### 💡 Core Intuition
Slide a window of size K: add the new element entering from the right, subtract the element leaving from the left. Maintain a running aggregate.

```
window_sum = sum(arr[:K])
result = [window_sum]
for i in range(K, n):
    window_sum += arr[i] - arr[i - K]
    result.append(window_sum)
```

> 🎯 For **permutation matching** (fixed window + character frequency): use a frequency map and a "matched" counter to check validity in O(1) per slide.

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) or O(Σ) for character frequency |

---

### PATTERN 2 — Variable-Length Window

#### 🧠 Recognize It When…
- "Longest/shortest subarray/substring satisfying a condition."
- The window expands when valid and **shrinks** from the left when the condition is violated.

#### 💡 Core Intuition
Use `left` and `right` pointers. Expand `right` unconditionally. When the window becomes **invalid**, advance `left` until valid again. The answer is updated whenever the window is valid.

```
left = 0
for right in range(n):
    # Expand window: include arr[right]
    window.add(arr[right])

    # Shrink window while invalid
    while window is not valid:
        window.remove(arr[left])
        left++

    # Window [left..right] is now valid
    answer = max(answer, right - left + 1)
```

> ⚡ **At-Most K trick**: If asked for subarrays with **exactly K** distinct elements, compute: `f(exactly K) = f(at most K) - f(at most K-1)`.

| | Complexity |
|--|--|
| Time | O(n) amortized — each element added/removed once |
| Space | O(K) or O(Σ) |

# 📖 Theory Roadmap: Divide & Conquer + Binary Search

> 🔗 **[← Back to Problem List](./readme.md)**
>
> D&C and Binary Search are two sides of the same coin — both **split** the problem space in half. Mastering them means mastering O(log N) thinking.

---

## 🔑 The Master Theorem (Quick Reference)

For a recurrence `T(n) = aT(n/b) + f(n)`:

| Condition | Result |
|-----------|--------|
| `f(n) = O(n^(log_b(a) - ε))` | T(n) = **Θ(n^log_b(a))** |
| `f(n) = Θ(n^log_b(a))` | T(n) = **Θ(n^log_b(a) · log n)** |
| `f(n) = Ω(n^(log_b(a) + ε))` | T(n) = **Θ(f(n))** |

**Examples**:  
- MergeSort: `T(n) = 2T(n/2) + O(n)` → **O(n log n)**  
- Binary Search: `T(n) = T(n/2) + O(1)` → **O(log n)**

---

## PATTERN 1 — The Foundations: Sorting & Linear Searching

---

### 🧠 Recognize It When…
- Sort an array in O(n log n).
- Search in a sorted array in O(log n).
- "Find first/last occurrence of X", "find insertion position."

---

### 💡 MergeSort

Split into two halves → sort each recursively → **merge** the sorted halves.

```
function mergeSort(arr, lo, hi):
    if lo >= hi: return
    mid = (lo + hi) // 2
    mergeSort(arr, lo, mid)
    mergeSort(arr, mid+1, hi)
    merge(arr, lo, mid, hi)     # merge two sorted halves

function merge(arr, lo, mid, hi):
    left  = arr[lo..mid]
    right = arr[mid+1..hi]
    i = j = 0; k = lo
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: arr[k] = left[i]; i++
        else:                   arr[k] = right[j]; j++
        k++
    fill remaining
```

| | Complexity |
|--|--|
| Time | O(n log n) — all cases |
| Space | O(n) auxiliary |

---

### 💡 Binary Search — Universal Template

> 🎯 **Core Principle**: Each iteration eliminates **half** the search space by checking the **midpoint**.

```
lo, hi = 0, len(arr) - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
return -1   # not found
```

**Left-most occurrence** (first position where `arr[mid] >= target`):
```
lo, hi = 0, n
while lo < hi:
    mid = (lo + hi) // 2
    if arr[mid] < target: lo = mid + 1
    else: hi = mid
return lo
```

| | Complexity |
|--|--|
| Time | O(log n) |
| Space | O(1) |

---

## PATTERN 2 — Mathematical D&C & Recursion

---

### 🧠 Recognize It When…
- Compute `base^exp mod M` efficiently.
- Recursive structure with subproblems of size `n/2`.
- Tower of Hanoi, matrix exponentiation.

---

### 💡 Fast Exponentiation (Binary Exponentiation)

Split the exponent in half: `x^n = x^(n/2) * x^(n/2)` (even) or `x * x^(n-1)` (odd).

```
function fastPow(base, exp, mod):
    if exp == 0: return 1
    if exp % 2 == 0:
        half = fastPow(base, exp // 2, mod)
        return (half * half) % mod
    else:
        return (base * fastPow(base, exp - 1, mod)) % mod
```

| | Complexity |
|--|--|
| Time | O(log exp) |
| Space | O(log exp) stack |

---

### 💡 Tower of Hanoi

Move N disks from `src` to `dst` using `aux`:
1. Move top N-1 disks from `src` to `aux`.
2. Move the largest disk from `src` to `dst`.
3. Move N-1 disks from `aux` to `dst`.

```
function hanoi(n, src, dst, aux):
    if n == 1: move(src → dst); return
    hanoi(n-1, src, aux, dst)
    move(src → dst)
    hanoi(n-1, aux, dst, src)
```

> Minimum moves = `2^n - 1`. Recurrence: `T(n) = 2T(n-1) + 1` → **O(2^n)**

---

### 💡 Matrix Exponentiation (Fibonacci in O(log n))

Represent the Fibonacci recurrence as a matrix equation:  
`[F(n+1), F(n)] = [[1,1],[1,0]]^n × [F(1), F(0)]`

Use fast matrix exponentiation with the same binary splitting trick.

| | Complexity |
|--|--|
| Naive Fibonacci | O(n) |
| Matrix Expo | O(log n) |

---

## PATTERN 3 — Grid, Geometry & QuadTrees

---

### 🧠 Recognize It When…
- Spatial subdivision: break a 2D grid into quadrants recursively.
- Closest pair of points in a plane.
- K closest points.

---

### 💡 Closest Pair of Points

1. Sort by x-coordinate.
2. Split into left/right halves. Recurse to get `d = min(d_left, d_right)`.
3. Check the **strip** of width `2d` around the midpoint for cross-pairs.

```
function closestPair(points, lo, hi):
    if hi - lo <= 3: brute force; return min_dist
    mid = (lo + hi) // 2
    d = min(closestPair(points, lo, mid),
            closestPair(points, mid, hi))
    # Check strip
    strip = [p for p in points if |p.x - midpoint.x| < d]
    sort strip by y
    for each point in strip, compare with next 7 neighbors
    return min(d, strip_min)
```

| | Complexity |
|--|--|
| Time | O(n log n) |
| Space | O(n) |

---

### 💡 QuickSelect (K-th Smallest / K Closest)

Partition the array around a pivot (like QuickSort). Only recurse into the partition that contains the K-th element.

```
function quickSelect(arr, lo, hi, k):
    pivot_idx = partition(arr, lo, hi)   # Lomuto/Hoare
    if pivot_idx == k: return arr[k]
    elif k < pivot_idx: return quickSelect(arr, lo, pivot_idx-1, k)
    else:               return quickSelect(arr, pivot_idx+1, hi, k)
```

| | Average | Worst |
|--|--|--|
| Time | O(n) | O(n²) |
| Space | O(log n) | O(n) |

---

## PATTERN 4 — Binary Search on Answer (The Feasible Pattern)

---

### 🧠 Recognize It When…
- "What is the **minimum** X such that some condition is satisfied?"
- You can write a `feasible(mid)` function that returns True/False.
- The answer space is **monotone**: False, False, ..., True, True, ...

---

### 💡 Core Template

```
lo, hi = MIN_ANSWER, MAX_ANSWER
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid        # try to do better (smaller)
    else:
        lo = mid + 1    # not enough, increase

return lo   # first value where feasible() is True
```

> 🔑 **How to define `lo` and `hi`**: Think about the **physical meaning** of the answer. For "min days to make M bouquets", lo=1 (min possible days), hi=max(arr) (worst case). For "capacity to ship in D days", lo=max(weights), hi=sum(weights).

> 🔑 **How to write `feasible(mid)`**: Simulate the problem with `mid` as the answer and check if it works. Usually O(n).

**Example — Koko Eating Bananas:**
```
def feasible(speed):
    hours = sum(ceil(pile / speed) for pile in piles)
    return hours <= H

lo, hi = 1, max(piles)
# Binary search for minimum feasible speed
```

| | Complexity |
|--|--|
| Time | O(n log(hi - lo)) |
| Space | O(1) |

---

## PATTERN 5 — Searching in Rotated or Peak Arrays

---

### 🧠 Recognize It When…
- Sorted array was **rotated** at some unknown pivot.
- Find a "peak" element (greater than its neighbors).

---

### 💡 Rotated Sorted Array

Key insight: when you split, **at least one half is always sorted**. Use this to decide which half to search.

```
lo, hi = 0, n - 1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target: return mid

    # Left half is sorted
    if arr[lo] <= arr[mid]:
        if arr[lo] <= target < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    # Right half is sorted
    else:
        if arr[mid] < target <= arr[hi]:
            lo = mid + 1
        else:
            hi = mid - 1
return -1
```

---

### 💡 Find Peak Element

Any peak works. Binary search: if `arr[mid] < arr[mid+1]`, a peak must exist to the right. Otherwise, to the left or at `mid`.

```
lo, hi = 0, n - 1
while lo < hi:
    mid = (lo + hi) // 2
    if arr[mid] < arr[mid + 1]:
        lo = mid + 1   # peak is to the right
    else:
        hi = mid       # peak is here or to the left
return lo
```

| | Complexity |
|--|--|
| Time | O(log n) |
| Space | O(1) |

---

## PATTERN 6 — Advanced Merging & Selection

---

### 🧠 Recognize It When…
- K-th smallest across K sorted lists or a sorted matrix.
- Median of two sorted arrays.

---

### 💡 K-th Smallest in Sorted Matrix (Binary Search on Value)

The matrix is sorted row-wise and column-wise. Binary search on the **value** in range `[matrix[0][0], matrix[n-1][n-1]]`. Count how many elements are ≤ `mid` using a staircase walk.

```
lo, hi = matrix[0][0], matrix[n-1][n-1]
while lo < hi:
    mid = (lo + hi) // 2
    # Count elements ≤ mid
    count = 0; col = n - 1
    for row in range(n):
        while col >= 0 and matrix[row][col] > mid: col--
        count += col + 1
    if count < k: lo = mid + 1
    else:         hi = mid
return lo
```

---

### 💡 Median of Two Sorted Arrays (O(log(min(m,n))))

Binary search on the partition point of the smaller array. Find a cut such that the left half of the combined array has `(m+n)/2` elements and all left elements ≤ all right elements.

```
# Ensure arr1 is the smaller array
if m > n: swap(arr1, arr2)

lo, hi = 0, m
while lo <= hi:
    cut1 = (lo + hi) // 2
    cut2 = (m + n + 1) // 2 - cut1
    # Check if this is the valid partition
    if left1 <= right2 and left2 <= right1: found!
    elif left1 > right2: hi = cut1 - 1
    else: lo = cut1 + 1
```

| | Complexity |
|--|--|
| Time | O(log(min(m, n))) |
| Space | O(1) |

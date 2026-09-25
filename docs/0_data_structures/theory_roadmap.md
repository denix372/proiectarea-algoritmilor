# 📖 Theory Roadmap: Data Structures

> 🔗 **[← Back to Problem List](./readme.md)**
>
> This document is the **theory companion** to the problem roadmap. For each pattern you will find: how to recognize it, the core intuition, a pseudocode template, and complexities.

---

## 📦 SECTION 1: Sets & Arrays

---

### PATTERN 1 — HashSet Core Operations

#### 🧠 Recognize It When…
- The problem asks for **duplicates**, **intersections**, or **membership tests** in O(1).
- The word "distinct", "unique", or "already seen" appears.

#### 💡 Core Intuition
A **HashSet** gives O(1) average insert/lookup. Use it as a *seen* or *membership* set to avoid nested loops.

```
function hasDuplicate(arr):
    seen = empty set
    for x in arr:
        if x in seen → return True
        seen.add(x)
    return False
```

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert / Lookup | O(1) | O(n) |
| Space | O(n) | O(n) |

---

### PATTERN 2 — Cyclic Sort / Index-Based Placement

#### 🧠 Recognize It When…
- Array contains integers in range **[1, N]** or **[0, N]**.
- Asked to find missing / duplicate without extra space.

#### 💡 Core Intuition
Each number `x` belongs at index `x-1`. Swap elements to their "home" index. After one pass, any index where `arr[i] ≠ i+1` reveals the missing/duplicate value.

```
function cyclicSort(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1          # correct index for arr[i]
        if arr[i] ≠ arr[j]:
            swap(arr[i], arr[j])
        else:
            i += 1

    for i in range(len(arr)):
        if arr[i] ≠ i + 1 → report i+1 as missing
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) |

---

### PATTERN 3 — Matrix Manipulation & Traversal

#### 🧠 Recognize It When…
- 2D grid rotation, zero-propagation, or spiral order.
- In-place matrix modification required.

#### 💡 Core Intuition
**Rotate 90° clockwise** = Transpose then reverse each row.  
**Spiral** = Shrink four boundaries (top, bottom, left, right) as you consume each ring.

```
# Rotate 90° clockwise (in-place)
transpose(matrix)           # swap [i][j] ↔ [j][i]
for each row: reverse(row)

# Spiral traversal
top, bottom, left, right = 0, R-1, 0, C-1
while top ≤ bottom and left ≤ right:
    walk right along top row → top++
    walk down along right col → right--
    walk left along bottom row → bottom--
    walk up along left col → left++
```

| | Complexity |
|--|--|
| Time | O(m × n) |
| Space | O(1) for in-place |

---

### PATTERN 4 — Array Intervals Sorting

#### 🧠 Recognize It When…
- Input is a list of `[start, end]` intervals.
- Asked to **merge**, **insert**, or count overlaps.

#### 💡 Core Intuition
Sort by start time. Walk through; if the current interval overlaps the last merged one (`curr.start ≤ merged.end`), extend it. Otherwise, append it as a new interval.

```
sort intervals by start
merged = [intervals[0]]
for [s, e] in intervals[1:]:
    if s ≤ merged[-1].end:
        merged[-1].end = max(merged[-1].end, e)
    else:
        merged.append([s, e])
```

| | Complexity |
|--|--|
| Time | O(n log n) |
| Space | O(n) |

---

### PATTERN 5 — In-Place Reversal & Swapping

#### 🧠 Recognize It When…
- Array rotation or reversal with O(1) extra space.

#### 💡 Core Intuition
**Rotate array right by k** = Reverse all → Reverse first k → Reverse rest.

```
reverse(arr, 0, n-1)
reverse(arr, 0, k-1)
reverse(arr, k, n-1)
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) |

---

## 🔗 SECTION 2: Linked List

---

### PATTERN 1 — In-Place Reversal

#### 🧠 Recognize It When…
- Asked to reverse a full or partial linked list without extra space.

#### 💡 Core Intuition
Use three pointers: `prev`, `curr`, `next`. At each step, flip the `curr.next` pointer backward.

```
prev = null
curr = head
while curr ≠ null:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
return prev   # new head
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) |

---

### PATTERN 2 — Fast & Slow Pointers (Cycle & Middle)

#### 🧠 Recognize It When…
- Detect a **cycle**, find the **middle**, or find the **start of a cycle**.
- "Does the list loop?", "What is the k-th from end?"

#### 💡 Core Intuition
`slow` moves 1 step, `fast` moves 2 steps. They meet inside a cycle (Floyd's algorithm) or `fast` reaches null when there's no cycle. When they meet, reset `slow` to head → advance both 1 step at a time → they meet at the cycle start.

```
slow = fast = head
while fast ≠ null and fast.next ≠ null:
    slow = slow.next
    fast = fast.next.next
    if slow == fast → cycle detected

# Find cycle start
slow = head
while slow ≠ fast:
    slow = slow.next
    fast = fast.next
# slow == fast == cycle start
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) |

---

### PATTERN 3 — Dummy Nodes & Node Deletion

#### 🧠 Recognize It When…
- Deleting the **head** is a special case.
- Removing the N-th from end.

#### 💡 Core Intuition
A **sentinel/dummy node** before the head unifies edge cases (deleting head = deleting after dummy). For N-th from end: advance the fast pointer N steps, then move both until fast reaches the last node.

```
dummy = Node(0)
dummy.next = head
prev = dummy

# Delete node with value val
while prev.next:
    if prev.next.val == val:
        prev.next = prev.next.next
    else:
        prev = prev.next
return dummy.next
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) |

---

### PATTERN 4 — Reordering & Advanced Manipulation

#### 🧠 Recognize It When…
- Interleave, segregate (odd/even), or rotate a list.
- Complex re-linking operations.

#### 💡 Core Intuition
**Odd-Even List**: Maintain two chains (odd-indexed, even-indexed), then link odd-tail → even-head.  
**Reorder List** (L0→Ln→L1→Ln-1): Find mid → Reverse second half → Merge two halves alternately.

```
# Odd-Even
odd = head; even = head.next; even_head = even
while even and even.next:
    odd.next = even.next; odd = odd.next
    even.next = odd.next; even = even.next
odd.next = even_head
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(1) |

---

### PATTERN 5 — Merging & Multiple Lists

#### 🧠 Recognize It When…
- Merge 2 or K sorted lists.
- Find intersection of two lists.

#### 💡 Core Intuition
**2 sorted lists**: Use a dummy head + compare heads, always linking the smaller one forward.  
**K sorted lists**: Use a min-heap of size K — pop the min node, push its successor.  
**Intersection**: Advance both pointers; when one reaches null, redirect to the other's head. They'll meet at the intersection after `|A| + |B|` steps each.

```
# Merge 2 sorted lists
dummy = Node(0); curr = dummy
while l1 and l2:
    if l1.val < l2.val: curr.next = l1; l1 = l1.next
    else:               curr.next = l2; l2 = l2.next
    curr = curr.next
curr.next = l1 or l2

# Merge K lists with min-heap
heap = [(list[i].val, i, list[i]) for i in range(K)]
heapify(heap)
while heap:
    val, i, node = heappop(heap)
    curr.next = node
    if node.next: heappush(heap, (node.next.val, i, node.next))
```

| Operation | Complexity |
|--|--|
| Merge 2 | O(m + n) time, O(1) space |
| Merge K | O(N log K) time, O(K) space |

---

## 📚 SECTION 3: Stacks & Queues

---

### PATTERN 1 — Bracket Matching & Stack Simulation

#### 🧠 Recognize It When…
- Validate/generate balanced parentheses, brackets, or decode a nested string.

#### 💡 Core Intuition
A **stack** tracks the "context" we're inside. Push on open; pop on close and validate matching.

```
stack = []
for char in s:
    if char in '([{':
        stack.push(char)
    else:
        if stack is empty or stack.top ≠ matching_open(char):
            return False
        stack.pop()
return stack is empty
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(n) |

---

### PATTERN 2 — Monotonic Stack: Next Greater / Smaller

#### 🧠 Recognize It When…
- "Find the next greater/smaller element for each position."
- "Span", "discount", "how many days until warmer."

#### 💡 Core Intuition
Maintain a stack of **indices** (not values) in decreasing order. When a new element is bigger than the stack top, that new element IS the "next greater" for everything it pops.

```
stack = []   # stores indices, kept in decreasing order of values
result = [-1] * n
for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        result[idx] = arr[i]   # arr[i] is the next greater for arr[idx]
    stack.push(i)
```

| | Complexity |
|--|--|
| Time | O(n) amortized (each element pushed/popped once) |
| Space | O(n) |

---

### PATTERN 3 — Monotonic Stack: Subarray Optimization & Histograms

#### 🧠 Recognize It When…
- Largest rectangle in histogram, sum of subarray minimums/maximums.
- "For each element, find how far left/right it is the minimum."

#### 💡 Core Intuition
Use a monotonic stack to efficiently find the **Previous Smaller Element (PSE)** and **Next Smaller Element (NSE)** for each bar. The width of the rectangle where bar `i` is the minimum is `NSE[i] - PSE[i] - 1`.

```
# Largest Rectangle in Histogram
stack = []
max_area = 0
for i in range(n + 1):
    h = heights[i] if i < n else 0
    while stack and heights[stack[-1]] > h:
        height = heights[stack.pop()]
        width  = i if not stack else i - stack[-1] - 1
        max_area = max(max_area, height * width)
    stack.push(i)
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(n) |

---

### PATTERN 4 — Monotonic Deque (Sliding Window Maximum)

#### 🧠 Recognize It When…
- Maximum (or minimum) in a **sliding window** of fixed size.
- Combined sliding window + constraint on range of values.

#### 💡 Core Intuition
A **deque** stores indices of "useful" candidates in decreasing order. The front is always the window's maximum. Before adding a new element, pop from the back any index whose value is smaller (it can never be a max again). Pop from the front any index that's outside the window.

```
deque = []   # indices, decreasing by value
result = []
for i in range(n):
    while deque and deque[0] < i - k + 1:
        deque.popleft()          # out of window
    while deque and arr[deque[-1]] < arr[i]:
        deque.pop()              # useless
    deque.append(i)
    if i >= k - 1:
        result.append(arr[deque[0]])
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(k) |

---

### PATTERN 5 — Object Design: Stacks & Queues

#### 🧠 Recognize It When…
- "Design a circular queue/deque with fixed capacity."
- Direct implementation of an abstract data type.

#### 💡 Core Intuition
Use a **fixed-size array** with `head` and `tail` pointers. All index arithmetic uses `% capacity`.

```
class CircularQueue:
    init(k): arr = [0]*k; head = -1; tail = -1; size = 0; cap = k

    enqueue(val):
        if size == cap: return False
        tail = (tail + 1) % cap
        arr[tail] = val
        if head == -1: head = 0
        size++; return True

    dequeue():
        if size == 0: return False
        if head == tail: head = tail = -1
        else: head = (head + 1) % cap
        size--; return True
```

| Operation | Complexity |
|--|--|
| Enqueue / Dequeue | O(1) |
| Space | O(k) |

---

## 🏔️ SECTION 4: Heaps / Priority Queues

---

### PATTERN 1 — Top K Pattern

#### 🧠 Recognize It When…
- "Find the K largest / K smallest / K most frequent elements."

#### 💡 Core Intuition
Maintain a **min-heap of size K**. For "K largest": push everything; if heap size exceeds K, pop (removes the smallest). The heap always holds the K largest seen so far.

```
heap = []
for x in arr:
    heappush(heap, x)
    if len(heap) > K:
        heappop(heap)   # remove smallest
return heap             # K largest elements
```

For **Top K frequent**: count frequencies first, then use the heap on `(count, element)` pairs.

| | Complexity |
|--|--|
| Time | O(n log K) |
| Space | O(K) |

---

### PATTERN 2 — Merge K Sorted Pattern

#### 🧠 Recognize It When…
- K sorted lists/arrays need to be merged or the K-th smallest element is needed across all of them.

#### 💡 Core Intuition
Seed a min-heap with the **first element from each of the K lists**. Each pop gives the global minimum; then push that list's next element.

```
heap = [(lists[i][0], i, 0) for i in range(K)]
heapify(heap)
result = []
while heap:
    val, list_i, elem_j = heappop(heap)
    result.append(val)
    if elem_j + 1 < len(lists[list_i]):
        heappush(heap, (lists[list_i][elem_j+1], list_i, elem_j+1))
```

| | Complexity |
|--|--|
| Time | O(N log K) where N = total elements |
| Space | O(K) |

---

### PATTERN 3 — Two Heaps Pattern

#### 🧠 Recognize It When…
- **Running median** from a data stream.
- Median in a sliding window.

#### 💡 Core Intuition
Maintain a **max-heap** (left half) and a **min-heap** (right half). Balance them so `|left| - |right| ≤ 1`. The median is either the top of the larger half or the average of both tops.

```
max_heap = []  # negated values for max behavior
min_heap = []

def add(num):
    heappush(max_heap, -num)
    heappush(min_heap, -heappop(max_heap))   # balance
    if len(min_heap) > len(max_heap):
        heappush(max_heap, -heappop(min_heap))

def median():
    if len(max_heap) == len(min_heap): return (-max_heap[0] + min_heap[0]) / 2
    return -max_heap[0]
```

| | Complexity |
|--|--|
| Add | O(log n) |
| Median | O(1) |

---

### PATTERN 4 — Heap Simulation (Min Operations)

#### 🧠 Recognize It When…
- "Repeatedly process the largest/smallest element."
- Greedy decisions involving dynamic priority changes.

#### 💡 Core Intuition
Use a max- or min-heap to always get the optimal candidate in O(log n). Simulate the process step by step.

```
# Last Stone Weight: repeatedly smash two heaviest stones
heap = [-x for x in stones]   # max-heap via negation
heapify(heap)
while len(heap) > 1:
    y = -heappop(heap)
    x = -heappop(heap)
    if x != y:
        heappush(heap, -(y - x))
return -heap[0] if heap else 0
```

| | Complexity |
|--|--|
| Time | O(n log n) |
| Space | O(n) |

---

## 🌳 SECTION 5: Trees

---

### PATTERN 1 — Tree DFS: Pre/In/Postorder

#### 🧠 Recognize It When…
- Process nodes in a specific visit order (root-left-right, left-root-right, left-right-root).
- Build expressions, print paths, serialize trees.

#### 💡 Core Intuition
Recursion naturally models the call stack for DFS. Choose the order based on what information you need at each node.

```
function dfs(node):
    if node is null: return
    visit(node)          # Preorder: process here
    dfs(node.left)
    # visit(node)        # Inorder: process here
    dfs(node.right)
    # visit(node)        # Postorder: process here
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(h) — O(log n) balanced, O(n) skewed |

---

### PATTERN 2 — Level Order Traversal (BFS)

#### 🧠 Recognize It When…
- Process nodes level by level.
- "Right side view", "average per level", "zigzag order."

#### 💡 Core Intuition
Use a **queue**. At each step, record the current queue size (= nodes in current level), process exactly that many nodes, and enqueue their children.

```
queue = [root]
while queue:
    level_size = len(queue)
    level = []
    for _ in range(level_size):
        node = queue.popleft()
        level.append(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    result.append(level)
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(w) — w = max width |

---

### PATTERN 3 — Tree Construction & Restructuring

#### 🧠 Recognize It When…
- Build a tree from **two traversal arrays** (e.g., preorder + inorder).
- Flatten a tree into a linked list.

#### 💡 Core Intuition
**Preorder + Inorder → Tree**: The first element of preorder is always the root. Find it in inorder to split left and right subtrees. Recurse.

```
function build(preorder, inorder):
    if not preorder: return null
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left  = build(preorder[1:mid+1], inorder[:mid])
    root.right = build(preorder[mid+1:], inorder[mid+1:])
    return root
```

| | Complexity |
|--|--|
| Time | O(n²) naive / O(n) with hashmap |
| Space | O(n) |

---

### PATTERN 4 — Tree Properties & Comparison

#### 🧠 Recognize It When…
- Check if two trees are the same, symmetric, or subtrees.
- Compute height, count nodes, find balanced property.

#### 💡 Core Intuition
Almost all structural properties can be computed by a **postorder** DFS that returns information from children up to the parent.

```
# Max depth
function depth(node):
    if node is null: return 0
    return 1 + max(depth(node.left), depth(node.right))

# Same tree
function isSame(p, q):
    if not p and not q: return True
    if not p or not q:  return False
    return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(h) |

---

### PATTERN 5 — Root to Leaf Paths & Sums

#### 🧠 Recognize It When…
- "Does a path from root to leaf sum to target?"
- Collect all root-to-leaf paths or path numbers.

#### 💡 Core Intuition
DFS with a **running sum** or **current path** accumulated along the way. At a leaf, check the condition.

```
function pathSum(node, target, current):
    if node is null: return False
    current += node.val
    if node is leaf: return current == target
    return pathSum(node.left, target, current) or
           pathSum(node.right, target, current)
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(h) |

---

### PATTERN 6 — Ancestry & LCA

#### 🧠 Recognize It When…
- Find the **Lowest Common Ancestor (LCA)** of two nodes.
- "What is the deepest node that is an ancestor of both?"

#### 💡 Core Intuition
DFS returns `True` if the subtree contains either target. The LCA is the first node where both left **and** right return `True`, or the node itself is one of the targets while a subtree contains the other.

```
function lca(node, p, q):
    if node is null: return null
    if node == p or node == q: return node
    left  = lca(node.left, p, q)
    right = lca(node.right, p, q)
    if left and right: return node   # found both in different subtrees
    return left or right
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(h) |

---

### PATTERN 7 — Tree DP, Distances & Complex Paths

#### 🧠 Recognize It When…
- "Diameter", "maximum path sum" — paths that can go through any node (not just root-to-leaf).
- Need to pass information **up** from children and combine at a node.

#### 💡 Core Intuition
For each node, compute the best result **within** that subtree and also the best "arm" that can be extended **upward**. The global answer is updated at every node.

```
global_max = -inf

function dfs(node):
    if node is null: return 0
    left  = max(0, dfs(node.left))   # ignore negative paths
    right = max(0, dfs(node.right))
    # Update global answer: best path passing through this node
    global_max = max(global_max, left + right + node.val)
    # Return best single arm for parent
    return node.val + max(left, right)
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(h) |

---

### PATTERN 8 — BST Operations

#### 🧠 Recognize It When…
- Tree with BST property: `left.val < node.val < right.val`.
- Search, insert, delete, validate, in-order successor.

#### 💡 Core Intuition
BST in-order traversal gives a **sorted sequence**. Use the BST invariant to navigate in O(h) time: go left if target < current, right if target > current.

```
# Search
function search(node, val):
    if not node: return null
    if val == node.val: return node
    if val < node.val:  return search(node.left, val)
    return search(node.right, val)

# Validate BST (pass bounds)
function isValid(node, min=-inf, max=+inf):
    if not node: return True
    if not (min < node.val < max): return False
    return isValid(node.left, min, node.val) and
           isValid(node.right, node.val, max)
```

| Operation | Balanced BST | Skewed |
|--|--|--|
| Search/Insert/Delete | O(log n) | O(n) |

---

### PATTERN 9 — Trie (Prefix Tree)

#### 🧠 Recognize It When…
- String prefix queries: "does any word start with this prefix?"
- Autocomplete, word search in a dictionary.

#### 💡 Core Intuition
Each node in the Trie is a **map of characters to child nodes** plus an `is_end` flag. Insert character by character; search by following existing links.

```
class TrieNode:
    children = {}   # char → TrieNode
    is_end = False

class Trie:
    root = TrieNode()

    insert(word):
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    startsWith(prefix):
        node = root
        for ch in prefix:
            if ch not in node.children: return False
            node = node.children[ch]
        return True
```

| Operation | Complexity |
|--|--|
| Insert / Search | O(L) — L = word length |
| Space | O(Σ × N × L) |

---

## 🔢 SECTION 6: HashTables

---

### PATTERN 1 — Frequency Counting & Basic Mapping

#### 🧠 Recognize It When…
- Count occurrences of characters, words, or numbers.
- "Most frequent", "first unique", "valid anagram."

#### 💡 Core Intuition
Use `dict` / `Counter` to build a frequency map in O(n). Then query or compare in O(n).

```
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

| | Complexity |
|--|--|
| Build | O(n) |
| Query | O(1) average |

---

### PATTERN 2 — Grouping & Advanced Mapping

#### 🧠 Recognize It When…
- "Group anagrams", "isomorphic strings", "word pattern matching."
- Different strings share the same canonical form.

#### 💡 Core Intuition
Map each item to a **canonical key** (e.g., sorted string for anagrams, or a normalized pattern like `0 1 0 2`). Group all items with the same key.

```
groups = defaultdict(list)
for word in words:
    key = ''.join(sorted(word))   # canonical form for anagram
    groups[key].append(word)
return list(groups.values())
```

---

### PATTERN 3 — Pairs & Tuple Sums

#### 🧠 Recognize It When…
- "Two numbers that sum to k" when array is **not sorted**.
- 4Sum II, count pairs with given difference.

#### 💡 Core Intuition
Store values seen so far in a hash map. For each element, check if the **complement** (`target - x`) already exists.

```
seen = {}
for x in arr:
    complement = target - x
    if complement in seen:
        return True
    seen[x] = True
```

| | Complexity |
|--|--|
| Time | O(n) |
| Space | O(n) |

---

### PATTERN 4 — Design: Hash Maps & Caches

#### 🧠 Recognize It When…
- Design an LRU/LFU Cache, or a custom HashMap.
- O(1) insert, delete, and random access simultaneously.

#### 💡 Core Intuition
**LRU Cache**: Combine a **HashMap** (key → node) with a **Doubly Linked List** (to track recency). On access, move the node to the head. On eviction, remove the tail.

```
class LRUCache:
    map = {}            # key → DLinkedNode
    head, tail = dummy nodes

    get(key):
        if key not in map: return -1
        move_to_head(map[key])
        return map[key].value

    put(key, value):
        if key in map:
            map[key].value = value
            move_to_head(map[key])
        else:
            node = DLinkedNode(key, value)
            map[key] = node; add_to_head(node)
            if len(map) > capacity:
                tail = remove_tail(); del map[tail.key]
```

| Operation | Complexity |
|--|--|
| get / put | O(1) |
| Space | O(capacity) |

---

## 🔤 SECTION 7 & 8: Strings & Sorting (Key Patterns)

---

### PATTERN — Palindrome Detection & Expansion

#### 🧠 Recognize It When…
- Count or find palindromic substrings/subsequences.

#### 💡 Core Intuition
**Expand Around Center**: For each position, expand outward checking symmetry. Do this for both odd (`i, i`) and even (`i, i+1`) centers.

```
function expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left--; right++
    return right - left - 1   # length of palindrome
```

| | Complexity |
|--|--|
| Time | O(n²) |
| Space | O(1) |

---

### PATTERN — Custom Sorting & Comparators

#### 🧠 Recognize It When…
- Sort by a non-standard criterion (frequency, concatenation result, custom rule).

#### 💡 Core Intuition
Define a **key function** or a **comparator**. For "Largest Number": compare two strings `a` and `b` by checking if `a+b > b+a`.

```
from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a: return -1   # a comes first
    return 1

sorted_nums = sorted(nums_as_str, key=cmp_to_key(compare))
```

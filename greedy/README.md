# 📌 Greedy Algorithms — Complete Roadmap

In a Greedy algorithm, we make the best choice available right now (the local optimum) and never look back. It works when the problem has the Greedy Choice Property—meaning a series of local bests leads to the absolute best result (the global optimum)

---

## Phase 1 — Foundations & Simple Selection
**Concept:** Verificarea fiecărui element și luarea unei decizii binare (da/nu) bazată pe o condiție simplă.

### 🔥 Standard (Core Mechanics)
- Maximum Sum Subsequence — Logic: Pick all positive numbers; if all are negative, pick the largest one.
- LeetCode 455: Assign Cookies — https://leetcode.com/problems/assign-cookies/
- LeetCode 1005: Maximize Sum Of Array After K Negations — https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
- LeetCode 860: Lemonade Change — https://leetcode.com/problems/lemonade-change/

### 🧩 Practice
- LeetCode 179: Largest Number — https://leetcode.com/problems/largest-number/
- LeetCode 406: Queue Reconstruction by Height — https://leetcode.com/problems/queue-reconstruction-by-height/
- LeetCode 881: Boats to Save People — https://leetcode.com/problems/boats-to-save-people/
- LeetCode 2160: Minimum Sum of Four Digit Number After Splitting Digits — https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

### 🌀 Niche
- LeetCode 1221: Split a String in Balanced Strings — https://leetcode.com/problems/split-a-string-in-balanced-strings/
- LeetCode 1403: Minimum Subsequence in Non-Increasing Order — https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

---

## Phase 2 — Intervals & Scheduling
**Concept:** Segmentarea timpului sau spațiului. Alegerea optimă depinde de sortarea după **End Times** pentru a lăsa cât mai mult spațiu liber.

### 🔥 Standard
- Activity Selection (The Spectacle Problem) — Logic: Sort by End Time.
- LeetCode 452: Minimum Number of Arrows to Burst Balloons — https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
- LeetCode 435: Non-overlapping Intervals — https://leetcode.com/problems/non-overlapping-intervals/
- LeetCode 56: Merge Intervals — https://leetcode.com/problems/merge-intervals/

### 🧩 Practice
- LeetCode 252 & 253: Meeting Rooms I & II
- LeetCode 646: Maximum Length of Pair Chain — https://leetcode.com/problems/maximum-length-of-pair-chain/
- LeetCode 763: Partition Labels — https://leetcode.com/problems/partition-labels/
- LeetCode 1024: Video Stitching — https://leetcode.com/problems/video-stitching/

### 🌀 Niche
- LeetCode 1288: Remove Covered Intervals — https://leetcode.com/problems/remove-covered-intervals/
- LeetCode 621: Task Scheduler — https://leetcode.com/problems/task-scheduler/

---

## Phase 3 — Resource Optimization (Knapsack & Refills)
**Concept:** Optimizarea raportului "bang for your buck" (profit/greutate) într-o capacitate limitată.

### 🔥 Standard
- Fractional Knapsack (Problema Rucsacului) — Logic: Pick items with the highest Value/Weight ratio.
- Gas Station (The Distance Problem) — Logic: Go as far as your tank allows and stop at the last possible station.
- The Florist Problem — $K$ people buying $N$ flowers. Logic: Buy most expensive flowers first.

### 🧩 Practice
- LeetCode 134: Gas Station — https://leetcode.com/problems/gas-station/
- LeetCode 871: Minimum Number of Refueling Stops — https://leetcode.com/problems/minimum-number-of-refueling-stops/
- LeetCode 135: Candy (Two-Pass Greedy) — https://leetcode.com/problems/candy/
- Dishonest Sellers (LeetCode/Codeforces) — Based on current vs. future price difference.

### 🌀 Niche
- LeetCode 1717: Maximum Score From Removing Substrings — https://leetcode.com/problems/maximum-score-from-removing-substrings/
- LeetCode 502: IPO (Priority Queue + Greedy) — https://leetcode.com/problems/ipo/

---

## Phase 4 — Deadlines & Profits (Job Sequencing)
**Concept:** Gestionarea task-urilor cu deadline-uri. Strategia este să amâni execuția unui task cât mai mult posibil pentru a nu bloca task-urile timpurii.

### 🔥 Standard
- Job Sequencing with Deadlines (ACS Homework Problem) — Logic: Sort by profit, place in the latest available slot.
- LeetCode 630: Course Schedule III — https://leetcode.com/problems/course-schedule-iii/

### 🧩 Practice
- LeetCode 1383: Maximum Performance of a Team — https://leetcode.com/problems/maximum-performance-of-a-team/
- LeetCode 1833: Maximum Ice Cream Bars — https://leetcode.com/problems/maximum-ice-cream-bars/

---

## Phase 5 — Number & String Construction
**Concept:** Construirea rezultatului lexicografic optim prin alegeri locale la nivel de caracter sau cifră.

### 🔥 Standard
- LeetCode 402: Remove K Digits (Monotonic Stack + Greedy) — https://leetcode.com/problems/remove-k-digits/
- LeetCode 738: Monotone Increasing Digits — https://leetcode.com/problems/monotone-increasing-digits/

### 🧩 Practice
- LeetCode 316: Remove Duplicate Letters — https://leetcode.com/problems/remove-duplicate-letters/
- LeetCode 670: Maximum Swap — https://leetcode.com/problems/maximum-swap/
- LeetCode 1081: Smallest Subsequence of Distinct Characters — https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

---

## Phase 6 — Advanced Greedy (Graphs & Heaps)
**Concept:** Logica Greedy aplicată în algoritmi clasici de grafuri sau structuri avansate de date.

### 🔥 Standard
- Huffman Coding: Combining smallest frequencies to build an optimal tree.
- Kruskal’s Algorithm: MST using cheapest edges (DSU).
- Prim’s Algorithm: MST growing from a node using cheapest adjacent edges.

### 🧩 Practice
- Dijkstra’s Algorithm: Shortest path by always visiting the closest unvisited node.
- LeetCode 1167: Minimum Cost to Connect Sticks — https://leetcode.com/problems/minimum-cost-to-connect-sticks/
- LeetCode 767: Reorganize String — https://leetcode.com/problems/reorganize-string/

---

**🎯 TOTAL: 44 Problems**



Sources:
https://leetcode.com/discuss/post/7344979/15-core-greedy-patterns-for-coding-inter-a1wp/
https://huaguo.substack.com/p/greedy-algorithm?r=39jyox&utm_campaign=post&utm_medium=web&triedRedirect=true
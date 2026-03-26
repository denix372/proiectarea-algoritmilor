from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        count_max = sum(1 for v in freq.values() if v == max_freq)

        part1 = (max_freq - 1) * (n + 1) + count_max
        return max(len(tasks), part1)

tasks = ["A","A","A","B","B","B"]
n = 2
print(Solution().leastInterval(tasks, n))
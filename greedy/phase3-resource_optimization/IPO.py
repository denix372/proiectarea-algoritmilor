from typing import List
from heapq import heappush, heappop, heapify
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        heapify(projects)
        available = []

        for _ in range(k):
            while projects and projects[0][0] <= w:
                cap, prof = heappop(projects)
                heappush(available, -prof)

            if not available:
                break

            w += -heappop(available)

        return w

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
print(Solution().findMaximizedCapital(k, w, profits, capital))
from typing import List
from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x : (x[0], -x[1]))
        heights = [envelopes[i][1] for i in range(n)]

        sol = []
        for i in range(n):
            j = bisect_left(sol, heights[i])
            if j == len(sol):
                sol.append(heights[i])
            else:
                sol[j] = heights[i]
        return len(sol)
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(Solution().maxEnvelopes(envelopes))
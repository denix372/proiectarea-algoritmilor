from typing import List
from heapq import heappush, heappop

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        q = []
        for i in range(len(mat)):
            s = sum(mat[i])
            heappush(q, (s, i))
        res = []
        for _ in range(k):
            _, x = heappop(q)
            res.append(x)
        return res

mat = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
k = 3
print(Solution().kWeakestRows(mat, k))
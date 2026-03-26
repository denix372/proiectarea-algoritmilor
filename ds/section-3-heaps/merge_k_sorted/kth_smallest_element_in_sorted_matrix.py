from typing import List
from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        q = []
        for i in range(min(k, n)):
            heappush(q, (matrix[i][0], i, 0))

        res = -1
        for _ in range(k):
            res, i, j = heappop(q)
            if j + 1 < m:
                heappush(q, (matrix[i][j + 1], i, j + 1))
        return res

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(Solution().kthSmallest(matrix, k))
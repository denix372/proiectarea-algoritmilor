from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n-1][n-1]

        while lo < hi:
            mid = (lo + hi) // 2
            count = 0
            col = n - 1

            # count how many numbers <= mid
            for row in range(n):
                while col >= 0 and matrix[row][col] > mid:
                    col -= 1
                count += col + 1

            if count < k:
                lo = mid + 1
            else:
                hi = mid

        return lo
    
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print(Solution().kthSmallest(matrix, k))
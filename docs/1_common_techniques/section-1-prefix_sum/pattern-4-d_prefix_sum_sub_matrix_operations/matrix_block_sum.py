
class Solution:
    def matrix_block_sum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        n = len(mat)
        m = len(mat[0])
        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix[i][j] =  (prefix[i - 1][j] 
                                 + prefix[i][j - 1] 
                                 - prefix[i - 1][j - 1]
                                 + mat[i - 1][j - 1])

        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(n - 1, i + k), min(m - 1, j + k)

                res[i][j] = (prefix[r2 + 1][c2 + 1] 
                              - prefix[r1][c2 + 1] 
                              - prefix[r2 + 1][c1] 
                              + prefix[r1][c1])
        return res

mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(Solution().matrixBlockSum(mat, k))
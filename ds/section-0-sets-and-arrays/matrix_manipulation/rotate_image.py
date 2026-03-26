from typing import List

class Solution:
    def rotate(self, mat: list[list[int]]) -> None:
        n = len(mat)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                up_left = mat[i][j]
                up_right = mat[j][n - 1 - i]
                down_right = mat[n - 1 - i][n - 1 - j]
                down_left = mat[n - 1 - j][i]

                mat[i][j] = down_left
                mat[j][n - 1 - i] = up_left
                mat[n - 1 - i][n - 1 - j] = up_right
                mat[n - 1 - j][i] = down_right

matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)
print(matrix)
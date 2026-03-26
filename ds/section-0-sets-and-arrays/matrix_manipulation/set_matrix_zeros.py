
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_col = False
        
        # 1. use first column nd first row as marks
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # 2: set the inside elements without the first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    
        # 3: set the first row if needed
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
                
        # 4: set first column if needed
        if first_col:
            for i in range(m):
                matrix[i][0] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
print(matrix)
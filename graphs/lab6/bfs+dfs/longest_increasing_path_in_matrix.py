from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        # dfs with memoization
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            longest = 1
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj

                if 0 <= ni < n and 0 <= nj < m:
                    if matrix[ni][nj] > matrix[i][j]:
                        longest = max(longest, 1 + dfs(ni, nj))
            
            memo[(i, j)] = longest
            return longest
        
        max_path = 0
        for i in range(n):
            for j in range(m):
                max_path = max(max_path, dfs(i, j))
        
        return max_path

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(Solution().longestIncreasingPath(matrix))
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

        dp[1][1] = grid[0][0]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if not (i == 1 and j == 1):
                    dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]
    
def minPathSumReconstruct(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    dp[1][1] = grid[0][0]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if not (i == 1 and j == 1):
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])

    # reconstruct path
    path = []
    i, j = n, m

    while not (i == 1 and j == 1):
        path.append((i-1, j-1))

        # if we came from up
        if dp[i][j] == grid[i-1][j-1] + dp[i-1][j]:
            i -= 1
        else:
            j -= 1

    path.append((0, 0))
    path.reverse()

    return path

    
grid = [[1,3,1],[1,5,1],[4,2,1]]
sol = Solution()
print(sol.minPathSum(grid))
print(minPathSumReconstruct(grid))
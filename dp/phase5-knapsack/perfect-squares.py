class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        dp = [10**4 + 1] * (n + 1)
        dp[0] = 0
        for sq in squares:
            for j in range(sq, n + 1):
                    dp[j] = min(dp[j], dp[j - sq] + 1)
        return dp[n]

sol = Solution()
n = 12
print(sol.numSquares(n))
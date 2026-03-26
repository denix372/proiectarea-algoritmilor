from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
    
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
    
                # This guarantees that the left portion [i, m] can always 
                # be merged down into exactly 1 single pile.
                for m in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j],
                                dp[i][m] + dp[m + 1][j])
    
                # If the entire interval [i, j] can be merged down to 1 pile,
                # we do it now. The cost is the sum of all stones in [i, j].
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]
    
        return dp[0][n - 1]

stones = [3,2,4,1]
k = 2
print(Solution().mergeStones(stones, k))

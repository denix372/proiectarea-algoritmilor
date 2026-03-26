from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, - 1, -1):
            mx = 0 # local maximum
            best = 0

            for j in range(1, k + 1):
                if i + j > n:
                    break
                
                mx = max(mx, arr[i + j - 1])
                dp[i] = max(dp[i], mx * j  + dp[i + j])
                # best track the best possible sum starting at i

        return dp[0]

arr = [1,15,7,9,2,5,10]
k = 3
sol = Solution()
print(sol.maxSumAfterPartitioning(arr, k))
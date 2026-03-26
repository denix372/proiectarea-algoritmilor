from typing import List
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            curr_max = 0
    
            for j in range(1, min(k, i) + 1):
                curr_max = max(curr_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + curr_max * j)

        return dp[n]

arr = [1,15,7,9,2,5,10]
k = 3
sol = Solution()
print(sol.maxSumAfterPartitioning(arr, k))
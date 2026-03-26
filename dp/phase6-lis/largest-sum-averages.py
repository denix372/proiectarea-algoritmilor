from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i

        for g in range(2, k + 1):
            for i in range(1, n + 1):
                for j in range(g - 1, i):
                    avg = (prefix[i] - prefix[j]) / (i - j)
                    dp[i][g] = max(dp[i][g], dp[j][g - 1] + avg)
                
        return max(dp[n])

nums = [9,1,2,3,9]
k = 3
print(Solution().largestSumOfAverages(nums, k))
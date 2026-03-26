from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for i in range(n)]
        for length in range(1, n):
            for i in range(n - length):
                j = i + length - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], 
                            dp[i][k - 1] + dp[k + 1][j]
                            + nums[i - 1] * nums[k] * nums[j + 1])
        return dp[1][n - 2]
        

sol = Solution()
nums = [3,1,5,8]
print(sol.maxCoins(nums))
from typing import List

# Target Sum – core idea:
#
# Assign each number either + or -.
# Let P = numbers with '+', N = numbers with '-'.
#
#   sum(P) - sum(N) = target
#   sum(P) + sum(N) = total
#
# Adding them:
#   2 * sum(P) = target + total
#
# So we need:
#   sum(P) = (target + total) / 2
#
# The problem becomes:
#   "How many subsets of nums sum to S?"
# where S = (target + total) // 2.
#
# This is 0/1 subset-sum counting.


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 == 1 or total < abs(target):
            return 0

        s = (total + target) // 2
        n = len(nums)
        dp = [[0] * (s + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(0, s + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][s]
        
    def findTargetSumWays_optimized(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2 == 1 or total < abs(target):
            return 0

        s = (total + target) // 2

        dp = [0] * (s + 1)
        dp[0] = 1

        for num in nums:
            for j in range(s, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[s]
        

nums = [1,1,1,1,1]
target = 3
sol = Solution()
print(sol.findTargetSumWays(nums, target))
print(sol.findTargetSumWays_optimized(nums, target))
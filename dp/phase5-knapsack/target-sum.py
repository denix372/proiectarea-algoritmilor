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
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = s // 2
        n = len(nums)

        dp = [[False] * (s + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            for j in range(s + 1):
                if j - nums[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][s]
        

# Optimized
def canPartition(nums):
    s = sum(nums)
    if s % 2 == 1:
        return False
    s = s // 2
    n = len(nums)

    dp = [False] * (s + 1) 
    dp[0] = True

    for num in nums:
        for j in range(s, num - 1, -1):
                dp[j] = dp[j] | dp[j - num]
    return dp[s]
        

sol = Solution()
nums = [1,5,11,5]
print(sol.canPartition(nums))
print(canPartition(nums))
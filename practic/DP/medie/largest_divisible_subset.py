from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [0] * n
        p = [-1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    p[i] = j
        sol = []
        i = dp.index(max(dp))
        while i != -1:
            sol.append(nums[i])
            i = p[i]
        sol.reverse()
        return sol

nums = [1,2,4,8]
print(Solution().largestDivisibleSubset(nums))
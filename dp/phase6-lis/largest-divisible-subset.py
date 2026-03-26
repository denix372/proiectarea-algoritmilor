from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        p = [-1] * n
        for i in range(1, n):
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

        
sol = Solution()
nums = [1,2,4,8]
print(sol.largestDivisibleSubset(nums))
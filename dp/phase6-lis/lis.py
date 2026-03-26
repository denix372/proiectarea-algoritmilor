import bisect
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# LIS in O(n log n)

def lis2(nums):
    sol = []
    n = len(nums)
    for i in range(n):
        j = bisect.bisect_left(sol, nums[i])
        if j == len(sol):
            sol.append(nums[i])
        else:
            sol[j] = nums[i]
    return len(sol)


# Reconstruction
def lis3(nums):
    n = len(nums)
    dp = [1] * n
    p = [-1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    p[i] = j
    sol = []
    i = dp.index(max(dp))
    while i != -1:
        sol.append(nums[i])
        i = p[i]
    sol.reverse()
    return sol


nums = [10,9,2,5,3,7,101,18]
sol = Solution()
print(sol.lengthOfLIS(nums))
print(lis2(nums))
print(lis3(nums))
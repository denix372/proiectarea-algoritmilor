from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            
        return max(dp)
    
#Reconstruction

def maxSubArrayReconstruction(nums):
    n = len(nums)
    dp = [0] * n
    p = [-1] * n # parents
    dp[0] = nums[0]

    for i in range(1, n):
        if nums[i] > dp[i - 1] + nums[i]:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i - 1] + nums[i]
            p[i] = i - 1 # update parents everytime we add a new element

    sol = max(dp)
    path = []
    i = dp.index(sol)
    while i != -1:
        path.append(nums[i])
        i = p[i]
    path.reverse()
    return path

def maxSubArrayOptimized(nums):
    n = len(nums)
    max_sum = nums[0]
    best_sum = nums[0]
    for i in range(1, n):
        max_sum = max(nums[i], max_sum + nums[i])
        best_sum = max(best_sum, max_sum)
    return best_sum


sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))
print(maxSubArrayOptimized(nums))
print(maxSubArrayReconstruction(nums))
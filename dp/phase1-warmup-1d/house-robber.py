from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

            
        return dp[n - 1]
    

#Optimized
def rob2(nums):
    rob1 = 0
    rob2 = 0

    for num in nums:
        temp = max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = temp
    
    return rob2

# Reconstruction
def rob3(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * n
    take = [False] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    take[0] = True
    take[1] = nums[1] > nums[0]

    for i in range(2, n):
        if dp[i - 2] + nums[i] > dp[i - 1]:
            dp[i] = dp[i - 2] + nums[i]
            take[i] = True
        else:
            dp[i] = dp[i - 1]
    path = []
    i = n - 1
    while i >= 0:
        if take[i]:
            path.append(nums[i])
            i -= 2
        else:
            i -= 1
            
    path.reverse()
    return path
        
        
nums = [2,7,9,3,1]
sol = Solution()
print(sol.rob(nums))
print(rob2(nums))
print(rob3(nums))
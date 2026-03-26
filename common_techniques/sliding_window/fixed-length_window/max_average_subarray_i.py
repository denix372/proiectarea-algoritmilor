
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        
        max_avg = (s / k)
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            max_avg = max(max_avg, (s / k))
        
        return max_avg

nums = [1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums, k))

class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        if k == 0:
            return nums
    
        n = len(nums)
        res = [-1] * n
        size = 2 * k + 1
        if n < size:
            return res

        s = 0
        for i in range(size):
            s += nums[i]

        res[k] = s // size
        for i in range(k + 1, n - k):
            s += nums[i + k] - nums[i - k - 1]
            res[i] = s // size
        
        return res

nums = [7,4,3,9,1,8,5,2,6]
k = 3
print(Solution().getAverages(nums, k))
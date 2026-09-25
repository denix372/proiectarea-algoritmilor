
class Solution:
    def min_sub_array_len(self, target: int, nums: list[int]) -> int:
        res, s, k = float("inf"), 0, 0
    
        for i in range(len(nums)):
            s += nums[i]
    
            while s >= target:
                res = min(res, i - k + 1)
                s -= nums[k]
                k += 1

        if res == float("inf"):
            return 0
        return res

target = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen(target, nums))
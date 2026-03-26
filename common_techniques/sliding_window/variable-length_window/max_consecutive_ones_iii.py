
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        j = 0
        res = 0
        cnt = 0 # count how many zeros are in window
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1

            while cnt > k:
                if nums[j] == 0:
                    cnt -= 1
                j += 1
            res = max(res, i - j + 1)

        return res

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(Solution().longestOnes(nums, k))
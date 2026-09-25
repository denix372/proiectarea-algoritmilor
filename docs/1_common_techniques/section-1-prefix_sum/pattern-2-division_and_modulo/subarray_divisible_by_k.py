from collections import defaultdict

class Solution:
    def subarrays_div_by_k(self, nums: list[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        cnt = 0
        prefix = 0

        for x in nums:
            prefix += x

            if prefix % k in d:
                cnt += d[prefix % k]
            d[prefix % k] += 1
        
        return cnt

nums = [4,5,0,-2,-3,1]
k = 5
print(Solution().subarraysDivByK(nums, k))
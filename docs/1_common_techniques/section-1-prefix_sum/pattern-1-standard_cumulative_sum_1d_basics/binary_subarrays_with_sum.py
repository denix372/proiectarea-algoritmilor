from collections import defaultdict

class Solution:
    def num_subarrays_with_sum(self, nums: list[int], goal: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        cnt = prefix = 0

        for x in nums:
            prefix += x
            if prefix - goal in d:
                cnt += d[prefix - goal]
    
            d[prefix] += 1

        return cnt

nums = [1,0,1,0,1]
goal = 2
print(Solution().numSubarraysWithSum(nums, goal))
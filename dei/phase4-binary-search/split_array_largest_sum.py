from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_transport(v, k, cap):
            trips = 1
            current = 0
            for x in v:
                if x > cap:
                    return False
                if current + x <= cap:
                    current += x
                else:
                    trips += 1
                    current = x
            return trips <= k

        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            if can_transport(nums, k, mid):
                high = mid
            else:
                low = mid + 1
        return low

nums = [7,2,5,10,8]
k = 2
print(Solution().splitArray(nums, k))
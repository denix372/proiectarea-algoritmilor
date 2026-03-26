from typing import List
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 1
        right = sum(time) * totalTrips

        def feasible(mid):
            res = 0
            for x in time:
                res += mid // x 
            return res >= totalTrips

        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

time = [1,2,3]
totalTrips = 5
print(Solution().minimumTime(time, totalTrips))
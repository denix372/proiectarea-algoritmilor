from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        cnt = 0
        end = -2**31 - 1
        for s, e in points:
            if s > end:
                end = e
                cnt += 1
        return cnt

points = [[1,2],[2,3],[3,4],[4,5]]
print(Solution().findMinArrowShots(points))
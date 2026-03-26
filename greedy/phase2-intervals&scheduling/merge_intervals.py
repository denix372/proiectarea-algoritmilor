from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start, end = intervals[0]
        for i in intervals:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                res.append([start, end])
                start, end = i[0], i[1]
        res.append([start, end])
        return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))